// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de Exercícios 2 CounterEx

/*
 * Class that implements a simple counter
 */
class Counter {
    private volatile int count=0;
    public void increment() { count++; };
    public int getCount() { return count; }
}

/*
 * Thread that implements a counter 1000 times
 */
class CountingThread extends Thread {
    public final int MAX_COUNT = 50000;
    private Counter counter;

    // It must be initialized like an object of the Counter type
    CountingThread(Counter counter) {
        this.counter = counter;
    }

    public void run(){
        // Each thread increments the counter 10.000 times
        for (int i = 0; i < MAX_COUNT; i++){
            counter.increment();
        }
    }
}

/*
 * This code has a behavior that depends on the relative chaining of each
 * executed operation by the threads.
 * This is commonly known as a race. 
 */

public class CounterEx {
    final static Counter counter = new Counter();

    public static void main(String[] args) throws InterruptedException {
        // Create the threads
        CountingThread t1 = new CountingThread(counter);
        CountingThread t2 = new CountingThread(counter);

        //Start the clock to check how long the iterations take
        long start = System.currentTimeMillis();

        //Initialize the threads
        t1.start();
        t2.start();

        // Await for the end of the threads
        t1.join();
        t2.join();

        // Stop the clock to check how long the iterations took
        long stop = System.currentTimeMillis();
        System.out.println("Elapsed time: " + (stop-start) + "ms");

        // Take care of possible errors in the count
        if (t1.MAX_COUNT + t2.MAX_COUNT != counter.getCount()){
            System.out.println("Erro na contagem!");
        }

        // Value of the counter has to be 20.000, correct? Let's try!
        System.out.println(counter.getCount());
        if (counter.getCount() !=10000 * Thread.activeCount()){
            throw new AssertionError("Contador INVÁLIDO!");
        }
    }

}
