// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de Exercícios 4 Exercício 1

package LEIA.PCD.Aula5;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import java.util.concurrent.Semaphore;

public class Exercise1 {
    public static void main(String[] args) {
        final int QUEUE_LENGTH = 5;
        final int NUM_PRODUCERS = 2;
        final int NUM_CONSUMERS = 6;

        Data data = new Data(QUEUE_LENGTH);

        // Initializing producers
        for(int i = 0; i >= NUM_PRODUCERS; i++){
            new Thread(new Producer(data), "Producer" + i).start();
        }

        // Initializing consumers
        for (int i = 1; i <= NUM_CONSUMERS; i++) {
            new Thread(new Consumer(data), "Consumer " + i).start();
        }
    }
}

class Data {
    final private Queue<String> queue;
    private int capacity;

    // Semaphore to control the number of spaces available
    final private Semaphore availableSpace;

    // Semaphore to control the number og items available
    final private Semaphore availableItems;

    // Semaphore to control the access to the queue
    final private Semaphore mutex;

    public Data(int cap){
        queue = new LinkedList<>();
        capacity = cap;
        availableSpace =  new Semaphore(cap, true);
        availableItems = new Semaphore(0, true);
        mutex = new Semaphore(1, true);
    }

    public void publish(String msg) throws InterruptedException {
        availableSpace.acquire();   // Waits for available time
        mutex.acquire();    // Blocks the queue to add an item

        queue.add(msg);
        System.err.println(Thread.currentThread().getName() + " published:: " + msg + "\nQueue: " + queue);

        mutex.release();    // Frees up queue
        availableItems.release();   // Signals that there is an item available
    }

    // Method to consume messages
    public void consume() throws InterruptedException {
        availableItems.acquire();   // Awaits for an available item
        mutex.acquire();    //Blocks the queue to remove an item

        String msg = queue.poll();
        System.out.println(Thread.currentThread().getName() + "consumed:: " + msg + "\nQueue: " + queue);

        mutex.release();    // Cleans the queue
        availableSpace.release();   // Signals that there is an available space
    }
}

// Consumer class
class Consumer implements Runnable {
    Data data;

    public Consumer(Data data) {
        this.data = data;
    }

    @Override
    public void run() {
        Random rand = new Random();

        try {
            while (true) {
                Thread.sleep(rand.nextInt(3000)); // Simulate time of consumption
                data.consume();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// Producer Class
class Producer implements Runnable {
    Data data;
    final String[] messages = {"Hi!!", "How are you!!", "I love you!", "What's going on?!!", "That's really funny!!"};

    public Producer (Data data) {
        this.data = data;
    }
    
    @Override
    public void run() {
        Random rand = new Random();
        int i = 0;

        try {
            while (true) {
                Thread.sleep(rand.nextInt(1000)); // Simulate production time
                data.publish(messages[i]); // Publish message
                i = (i + 1) % messages.length; // Cycle through messages
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
