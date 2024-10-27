// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// ExecutorService: future

package LEIA.PCD.Aula6;

import java.util.concurrent.*;

public class future {
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        ExecutorService executorService = Executors.newSingleThreadExecutor();

        // Submit one task and obtain a Future type object
        Future<String> future = executorService.submit(() -> {
            Thread.sleep(2000);
            return "Hello, World!";
        });

        // Complete other tasks while previous computing tasks are in progress

        // Await for the result and acquire it
        String result = future.get();
        System.out.println(result);

        // Shut down ExecutorService
        executorService.shutdown();
    }
}
