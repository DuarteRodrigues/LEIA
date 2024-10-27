// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// ExecutorService: Future Without ExecutorService

package LEIA.PCD.Aula6;

import java.util.concurrent.*;

public class futurewithoutexecutorservice {
    public static void main(String[] args) throws InterruptedException, ExecutionException{
        ExecutorService executorService = Executors.newSingleThreadExecutor();

        // Submit a task and obtain a Future type object
        FutureTask<Integer> futureTask = new FutureTask<Integer> (new Callable<Integer>() {
            @Override
            public Integer call() throws Exception {    // Callable defines a unique method call()
                Thread.sleep(2000);
                return 42;
            }
        });

        Thread t = new Thread(futureTask);
        t.start();

        // Complete other tasks while the previous computing process is in progress

        // Await for the result and obtain it
        Integer result = futureTask.get();
        System.out.println("The result was " + result);
    }
}
