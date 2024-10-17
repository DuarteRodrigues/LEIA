package LEIA.PCD.Aula5;

import java.util.Random;

public class Producer implements Runnable{
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
