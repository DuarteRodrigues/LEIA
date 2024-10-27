// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// ExecutorService: callable

package LEIA.PCD.Aula6;

import java.util.concurrent.*;

public class callable {
    public static void main(String[] args) throws InterruptedException, ExecutionException{
        ExecutorService executorService = Executors.newSingleThreadExecutor();

        // Submit a task and obtain a Future type object
        Future<Integer> future = executorService.submit(new Callable<Integer>(){ // Parameter with value type
            @Override
            public Integer call() throws Exception { // Callable defines a unique method call   ()
                Thread.sleep(2000);
                return 42;
            }
        });

        // Complete other tasks while the previous computing process is in progress

        // Await for the result and obtain it
        Integer result = future.get();
        System.out.println(result);

        // Shutdown ExecutorService
        executorService.shutdown();
    }
}