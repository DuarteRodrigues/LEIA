// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de exercícios 5 Exercício 3

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

    public void shutdown(){
        executorService.shutdown();
    }
}

public class Exercise3 {
    public static void main(String[] args) throws InterruptedException, ExecutionException{
        CubeCalculator calculator1 = new CubeCalculator();
        CubeCalculator calculator2 = new CubeCalculator();

        // Initiates the two calculators in parallel
        Future<Integer> future1 = calculator1.calculate(3);
        Future<Integer> future2 = calculator2.calculate(4);

        // While both calculators are not ready, show state
        while(!future1.isDone() || !future2.isDone()){
            String status1 = future1.isDone() ? "done" : "not done";
            String status2 = future2.isDone() ? "done" : "not done";
            System.out.println("calc1: " + status1 + "calc2: " + status2);
            Thread.sleep(500); // Awaits 500ms before checking again
        }

        // Prints the results of both calculators
        System.out.println("Result calc1: " + future1.get());
        System.out.println("Result calc2: " + future2.get());

        // Shutdown ExecutorServices
        calculator1.shutdown();
        calculator2.shutdown();
    }
}
