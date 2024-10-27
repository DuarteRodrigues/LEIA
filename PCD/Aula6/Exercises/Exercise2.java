// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de exercícios 5 Exercício 2

package LEIA.PCD.Aula6.Exercises;

import java.util.concurrent.*;

class CubeCalculator {
    final public ExecutorService executorService = Executors.newSingleThreadExecutor();

    public Future<Integer> calculate(Integer input){
        return executorService.submit(() -> {
            Thread.sleep(2000);
            return input * input * input;
        });
    }
}

public class Exercise2 {
    public static void main(String[] args) throws InterruptedException, ExecutionException{
        CubeCalculator calculator = new CubeCalculator();
        Future<Integer> future = calculator.calculate(5);

        int attempts = 0;
        boolean isCancelled = false;

        // While the result ins't ready, show 'Calculating'
        while(!future.isDone()){
            System.out.println("Calculating...");
            Thread.sleep(500); // Waits 500ms before checking again
            attempts++;

            // If the number of attempts surpasses 3(1.5 seconds), cancels the math
            if(attempts > 3){
                isCancelled = future.cancel(true); // Tries to cancel the math
                break;
            }
        }

        // Checks if the math has been cancelled and prints the appropriate message
        if (isCancelled) {
            System.err.println("Cancelled");
        } else {
            System.err.println("Result: " + future.get());
        }

        // Closes ExecutorService to free up recourses
        calculator.executorService.shutdown();
        
    }
}