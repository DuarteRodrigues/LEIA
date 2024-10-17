package LEIA.PCD.Aula5;

import java.util.LinkedList;
import java.util.Queue;

public class Data {
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
