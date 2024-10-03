public class Exercise3 {
    public static void main(String args[]) {
        // Create and initialize the Threads using lambda expressions for Runnable
        Thread nameThread = new Thread(() -> {
            try{
                while (!Thread.currentThread().isInterrupted()){
                    System.out.println("Duarte");
                    Thread.sleep(3000); // Wait 3 seconds
                }
            }
            catch(InterruptedException e){
                // Interrupted Thread, leaves loop
            } finally {
                System.out.println("Thread Nome Terminada");
            }
        });

        Thread surnameThread = new Thread (() -> {
            try{
                while (!Thread.currentThread().isInterrupted()){
                    System.out.println("Rodrigues");
                    Thread.sleep(5000);
                }
            }catch (InterruptedException e){
                // Interrupted Thread, leaves loop
            }finally{
                System.out.println("Thread Apelido Terminada");
            }
        });

        // Initiate Threads
        nameThread.start();
        surnameThread.start(); 

        try{
            Thread.sleep(150000); // Main task sleeps for 15 seconds
        } catch (InterruptedException e){
            e.printStackTrace();
        }

        // Interrupt the Threads
        nameThread.interrupt();
        surnameThread.interrupt();

        try {
            //Ensures the Threads are finished
            nameThread.join();
            surnameThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Tarefa principal terminada.");
    }
}
