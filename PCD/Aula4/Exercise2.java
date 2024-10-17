// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de Exercícios 3 Exercício 2

import java.util.Random;
import java.util.concurrent.atomic.AtomicInteger;

class Philosopher extends Thread{
    private AtomicInteger left, right;
    private Random random;

    public Philosopher(String name, AtomicInteger left, AtomicInteger right) {
        super(name);
        this.left = left;
        this.right = right;
        this.random = new Random();
    }

    @Override
    public void run() {
        try {
            while (true) { 
              System.out.println(this.getName() + " thinking...");
              Thread.sleep(random.nextInt(1000)); // Philosopher thinks for a while  

              // Tries to pick up two chopsticks
              if (pickupChopsticks()){
                // Eats after picking up two chopsticks
                System.out.println(this.getName()+ " eating...");
                Thread.sleep(random.nextInt(1000)); // Philosopher eats for a while

                // Release the chopsticks
                releaseChopsticks();
              } else {
                // If the philosopher can't pick up chopsticks, continues thinking
                System.out.println(this.getName() + " couldn't pick up chopsticks, continues thinking");
              }
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private boolean pickupChopsticks(){
        // Tries to pickup left and right chopsticks using compareAndSet()
        boolean gotLeft = left.compareAndSet(0, 1);
        boolean gotRight = right.compareAndSet(0, 1);
    
        // If grabbed both chopstick, return 'true'
        if (gotLeft && gotRight){
            return true;
        } else {
            // If couldn't grab both, release the one the philosopher grabbed first (if any)
            if(gotLeft){
                left.set(0); // Release the left chopstick
            }
            if (gotRight){
                right.set(0); // Release the right chopstick
            }
            return false; // Couldn't grab both, then cannot eat
        }
    }

    private void releaseChopsticks(){
        // Release both chopsticks, defining them as 0
        left.set(0);
        right.set(0);
        System.out.println(this.getName() + " put down both chopsticks.");
    }
}

public class Exercise2 {
    public static void main(String[] args) {
        final int NUM_PHILOS = 5;
        Philosopher[] philosophers = new Philosopher[NUM_PHILOS];
        AtomicInteger[] chopsticks = new AtomicInteger[NUM_PHILOS];

        // Initialize the chopsticks as AtomicIntegers (0 means available)
        for (int i = 0; i < NUM_PHILOS; i++) {
            chopsticks[i] = new AtomicInteger(0); // 0 = available, 1 = used 
        }

        // Initialize the philosophers
        for (int i = 0; i < NUM_PHILOS; i++) {
            philosophers[i] = new Philosopher("Philo" +  (i+1), chopsticks[i], chopsticks[(i+1) % NUM_PHILOS]);
            philosophers[i].start();
        }
    }
}