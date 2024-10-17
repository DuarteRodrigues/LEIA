package LEIA.PCD.Aula5;

import java.util.Random;

public class Consumer implements Runnable{
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