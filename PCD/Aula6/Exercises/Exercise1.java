// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de exercícios 5 Exercício 1

package LEIA.PCD.Aula6.Exercises;

import java.util.concurrent.*;

class CubeCalculator {
    final private ExecutorService executorService = Executors.newSingleThreadExecutor();

    public Future<Integer> calculate(Integer input){
        return executorService.submit(() -> {
            Thread.sleep(2000);
            return input * input * input;
        });
    }
}

public class Exercise1 {
    public static void main(String[] args) throws InterruptedException, ExecutionException{
        CubeCalculator calculator = new CubeCalculator();
        Future<Integer> future = calculator.calculate(5);

        // While the result ins't ready, show 'Calculating'
        while(!future.isDone()){
            System.out.println("Calculating...");
            Thread.sleep(500);
        }

        // When the math is complete, show result
        System.err.println("Result: " + future.get());
    }
}
