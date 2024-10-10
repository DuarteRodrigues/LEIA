// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de Exercícios 2 Exercício 0

public class Exercise0 {
    public static void main(String[] args){
        Exercise0 ex0 = new Exercise0();
        ex0.runExercise();
    }

    void runExercise(){
        int NUM_THREADS = 2;
        int NUM_INCS_PER_THREAD = 10000;
        Counter counter = new Counter();
        Thread[] threads = new Thread[NUM_THREADS];

        long startTime = System.nanoTime();

        for(int i = 0; i < NUM_THREADS; i++){
            threads[i] = new Thread(new IncrementerThread(counter, NUM_INCS_PER_THREAD));
            threads[i].start();
        }

        try {
            for (int i = 0; i < NUM_THREADS; i++) {
                threads[i].join();
            }
        } catch (InterruptedException e){
            e.printStackTrace();
        }

        long endTime = System.nanoTime();

        System.out.println("Running " + NUM_THREADS + "threads, " + NUM_INCS_PER_THREAD + " increments each.");
        System.out.println("Elapsed time: " + (endTime - startTime) / 1000 + " us");
        System.out.println("Expected7final count: " + NUM_THREADS * NUM_INCS_PER_THREAD + "/" + counter.getCounter());
    }

    class Counter {
        private int counter = 0;

        void increment(){
            counter++;
        }

        int getCounter(){
            return counter;
        }
    }

    class IncrementerThread implements Runnable {
        private Counter counter;
        private int incrementsPerThread;

        IncrementerThread(Counter counter, int incrementsPerThread) {
            this.counter = counter;
            this.incrementsPerThread = incrementsPerThread;
        }

        @Override
        public void run() {
            for (int i = 0; i < incrementsPerThread; i++) {
                counter.increment();
            }
        }
    }
}
