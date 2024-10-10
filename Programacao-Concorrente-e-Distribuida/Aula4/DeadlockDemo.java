// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de Exercícios 3 Exercício 0

import java.util.Random;

public class DeadlockDemo {
    public static void main(String[] args) {

        final int NUM_PHILOS = 5;
        final int NUM_CHOPSTICKS = NUM_PHILOS;
        Philosopher[] philosophers = new Philosopher[NUM_PHILOS];
        Chopstick[] chopstick = new Chopstick[NUM_CHOPSTICKS];

        // Create chopsticks
        for (int i = 0; i < NUM_CHOPSTICKS; i++) {
            chopstick[i] = new Chopstick();
        }

        // Create philosophers
        for (int i = 0; i < NUM_PHILOS; i++){
            philosophers[i] = new Philosopher("Philo" + (i+1), chopstick[i], chopstick[(i+1) % NUM_CHOPSTICKS]);
            philosophers[i].start();
        }
    }
}
class Chopstick extends Object{

}

class Philosopher extends Thread {
    final private Chopstick left, right;
    final private Random random;

    public Philosopher(String name, Chopstick left, Chopstick right){
        super(name);
        this.left = left;
        this.right = right;
        this.random = new Random();
    }

    @Override
    public void run() {
        try{
            while(true){
                System.out.println(this.getName() + " thinking...");
                Thread.sleep(random.nextInt(1000)); // Think for a while
                synchronized(left) { // Grab left chopstick
                    synchronized(right){ // Grab right chopstick
                        System.out.println(this.getName() + " eating...");
                        Thread.sleep(random.nextInt(1000)); // Eat for a while
                    }
                }
            }
        } catch (InterruptedException e){
            e.printStackTrace();
        } finally {

        }

    }
}
