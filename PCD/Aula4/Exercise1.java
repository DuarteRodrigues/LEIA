// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de Exercícios 3 Exercício 1

import java.util.Random;
import java.util.concurrent.Semaphore;

class Philosopher extends Thread{
    private Semaphore left, right;
    private Random random;

    public Philosopher(String name, Semaphore leftChopstick, Semaphore rightChopstick) {
        super(name);
        this.left = left;
        this.right = right;
        this.random = new Random();
    }

    @Override
    public void run() {
        try {
            while (true) {
                System.out.println(this.getName() + " is thinking...");
                Thread.sleep(random.nextInt(1000)); // Philosopher thinks for a while

                // Tries to pickup two stick
                left.acquire();
                System.out.println(this.getName() + " picked up left chopstick.");
                right.acquire();
                System.out.println(this.getName() + " picked up right chopstick.");

                // Eats only after picking up two chopsticks
                System.out.println(this.getName() + " is eating...");
                Thread.sleep(random.nextInt(1000)); // Philosopher eats for a while

                // Lets go of the chopsticks
                left.release();
                System.out.println(this.getName() + " put down left chopstick.");
                right.release();
                System.out.println(this.getName() + " put down right chopstick.");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class Exercise1 {
    public static void main(String[] args) {
        final int NUM_PHILOS = 5;
        Philosopher[] philosophers = new Philosopher[NUM_PHILOS];
        Semaphore[] chopsticks = new Semaphore[NUM_PHILOS];

        // Initialize the semaphores(chopsticks) as available
        for(int i = 0; i < NUM_PHILOS; i++){
            chopsticks[i] = new Semaphore(i); // Binary semaphore, indicating that the chopstick is available
        }

        // Initialize the philosophers
        for(int i = 0; i < NUM_PHILOS; i++){
            philosophers[i] = new Philosopher("Philo" + (i+1), chopsticks[i], chopsticks[(i+1) % NUM_PHILOS]);
            philosophers[i].start();
        }
    }
}
