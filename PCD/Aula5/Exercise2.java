// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de Exercícios 4 Exercício 2

package LEIA.PCD.Aula5;

import java.util.Random;
import java.util.concurrent.LinkedBlockingQueue;

public class Exercise2 {
    public static void main(String[] args) {
        final int NUM_CONSUMERS = 3; // Amount of consumers
        final int TOTAL_ITEMS = 100; // Item total that the producer will develop
        
        // Queue of linked blocks (LinkedBlockingQueue) to store ints
        LinkedBlockingQueue<Integer> queue = new LinkedBlockingQueue<>();
        
        // Initialize the producers
        Thread producerThread = new Thread(new Producer(queue, TOTAL_ITEMS), "Producer");
        producerThread.start();
        
        // Initialize the consumers
        for (int i = 1; i <= NUM_CONSUMERS; i++) {
            new Thread(new Consumer(queue, TOTAL_ITEMS), "Consumer " + i).start();
        }
    }
}

// Producer class
class Producer implements Runnable {
    private LinkedBlockingQueue<Integer> queue;
    private int totalItems;

    public Producer(LinkedBlockingQueue<Integer> queue, int totalItems) {
        this.queue = queue;
        this.totalItems = totalItems;
    }

    @Override
    public void run() {
        try {
            for (int i = 1; i <= totalItems; i++) {
                System.out.println(Thread.currentThread().getName() + " produced: " + i);
                queue.put(i); // Adds the int to queue
                Thread.sleep(50); // Simulate processing time
            }
            queue.put(-1); // Signals the end of production
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

// Consumer class
class Consumer implements Runnable {
    private LinkedBlockingQueue<Integer> queue;
    private int totalItems;

    public Consumer(LinkedBlockingQueue<Integer> queue, int totalItems) {
        this.queue = queue;
        this.totalItems = totalItems;
    }

    @Override
    public void run() {
        try {
            while (true) {
                Integer number = queue.take(); // Removes int from queue
                
                if (number == -1) { // Checks end of
                    queue.put(-1); // Signals the end of production to consumers
                    break;
                }
                
                System.out.println(Thread.currentThread().getName() + " consumed: " + number);
                Thread.sleep(new Random().nextInt(100)); // Simulates consumption time
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}