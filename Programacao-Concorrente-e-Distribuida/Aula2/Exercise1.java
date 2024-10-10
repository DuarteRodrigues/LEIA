// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Grupo de Exercícios 1 Exercício 1

class NameThread extends Thread {
    private String name;

    public NameThread(String name){
        this.name = name;
    }
    
    @Override
    public void run(){
        try{
            while(!Thread.currentThread().isInterrupted()){
                System.out.println(name);
                Thread.sleep(3000); // Waits 3 seconds
            }
        }
        catch (InterruptedException e){
            // Thread Interrupted, leaves loop
        }
        finally {
            System.out.println(name + "thread terminada");
        }
    }
}

class SurnameThread extends Thread{
    private String surname;

    public SurnameThread(String surname){
        this.surname = surname;
    }

    @Override
    public void run(){
        try{
            while(!Thread.currentThread().isInterrupted()){
                System.out.println(surname);
                Thread.sleep(3000); // Waits 3 seconds
            }
        }
        catch (InterruptedException e){
            // Thread Interrupted, leaves loop
        }
        finally {
            System.out.println(surname + "thread terminada");
        }
    }
}

public class Exercise1{
    public static void main(String[] args) {
        NameThread nameThread = new NameThread("Duarte");
        SurnameThread surnameThread = new SurnameThread("Rodrigues");

        nameThread.start();
        surnameThread.start();

        try{
            Thread.sleep(15000); // Waits 15 seconds
        }
        catch (InterruptedException e){
            e.printStackTrace();
        }

        nameThread.interrupt(); // interrupts name thread
        surnameThread.interrupt(); // Interrupts surname thread

        try {
            nameThread.join(); // Assures name thread finishes
            surnameThread.join(); // Assures surname thread finishes
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Tarefa principal terminada.");
    }
}