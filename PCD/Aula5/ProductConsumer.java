package LEIA.PCD.Aula5;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

public class ProductConsumer{
    public static void main(String[] args) {
        final int QUEUE_LENGTH = 5;
        final int NUM_PRODUCERS = 2;
        final int NUM_CONSUMERS = 6;

        Data data = new Data(QUEUE_LENGTH);
        
        for (int i = 1; i <= NUM_PRODUCERS; i++){
            new Thread(new Producer(data), "Producer " + i).start();
        }
 
        for (int i = 1; i <= NUM_CONSUMERS; i++){
            new Thread(new Consumer(data), "Consumer " + i).start();
        }
    }
}   

class Data{
    Queue<String> q;
    int capacity;
    
    Data(int cap) {
        q = new LinkedList<>();
        capacity = cap;
    }
 
    public synchronized void publish(String msg) throws InterruptedException {
        String name = Thread.currentThread().getName();
        while (q.size() == capacity) { // Repetition! All threads are notified.
            System.out.println("Queue Full! " + name + " waiting for message to be consumed...");
            wait();
        }

        q.add(msg);
        System.out.println("Message published:: " + msg + "\nQueue: "+ q + "\n");
        notifyAll();
    }

    public synchronized void consume() throws InterruptedException {
        String name = Thread.currentThread().getName();
        while (q.isEmpty()) { // Repetition! All threads are notified.
            System.out.println(name+" waiting for new message...");
            wait();
        }
        String msg = q.poll();
        System.out.println(name + " consumed msg:: " + msg + "\nQueue: "+ q + "\n");
        notifyAll();
    }
}

class Consumer implements Runnable{
    Data data;
    public Consumer(Data data) {
        this.data = data;
    }

    @Override
    public void run() {
        Random rand = new Random();
        try {
            while (true) {
                Thread.sleep(rand.nextInt(3000));
                data.consume();
            }
        } catch (InterruptedException e) {
            
        }
    }
    
}

class Producer implements Runnable{
    Data data;
    final String[] messages = { "Hi!!",
                                "How are you!!",
                                "I love you!",
                                "What's going on?!!",
                                "That's really funny!!"};
    public Producer(Data data) {
        this.data = data;
    }

    @Override
    public void run() {
        Random rand = new Random();
        int i = 0;
        try {
            while (true) {
                Thread.sleep(rand.nextInt(1000));
                data.publish(messages[i]);
                i = (i + 1) % messages.length;
            }
        } catch (InterruptedException e) {
            
        }
    }
}