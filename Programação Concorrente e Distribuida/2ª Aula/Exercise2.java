// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de Exercícios 1 Exercício 2

class NameThreadRunnable implements Runnable {
    private String name;

    public NameThreadRunnable(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        try {
            while (!Thread.currentThread().isInterrupted()) {
                System.out.println(name);
                Thread.sleep(3000); // Waits 3 seconds
            }
        } catch (InterruptedException e) {
            // Interrupted thread, leaves loop
        } finally {
            System.out.println(name + " thread terminada.");
        }
    }
}

class SurnameThreadRunnable implements Runnable {
    private String surname;

    public SurnameThreadRunnable(String surname) {
        this.surname = surname;
    }

    @Override
    public void run() {
        try {
            while (!Thread.currentThread().isInterrupted()) {
                System.out.println(surname);
                Thread.sleep(5000); // Waits 5 seconds
            }
        } catch (InterruptedException e) {
            // Interrupted thread, leaves loop
        } finally {
            System.out.println(surname + " thread terminada.");
        }
    }
}

public class Exercise2 {
 
    public static void main(String[] args) {
        // Create Runnable instances
        NameThreadRunnable nameRunnable = new NameThreadRunnable("Duarte");
        SurnameThreadRunnable surnameRunnable = new SurnameThreadRunnable("Rodrigues");

        // Initiate the Threads using Runnable instances
        Thread nameThread = new Thread(nameRunnable);
        Thread surnameThread = new Thread(surnameRunnable);

        nameThread.start();
        surnameThread.start();

        try {
            Thread.sleep(15000); // Main task sleeps for 15 minutes
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        nameThread.interrupt(); // Interrupts first name thread
        surnameThread.interrupt(); // Interupts surname thread

        try {
            nameThread.join(); // Ensures name thread is finished
            surnameThread.join(); // Ensures surname thread is finished
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Tarefa principal terminada.");
    }

}