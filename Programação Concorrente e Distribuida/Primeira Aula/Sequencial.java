public class Sequencial {
    
    public static void main(String[] args) throws InterruptedException{
        //Delay times
        final int DELAY1 = 5000;
        final int DELAY2 = 3000;

        int proximo1 = DELAY1;
        int proximo2 = DELAY2;

        // While loop
        while(true){
            if (proximo1 < proximo2) {
                Thread.sleep(proximo1);
                System.out.println("Duarte");
                proximo2 = proximo2 - proximo1;
                proximo1 = DELAY1;
            }
            else if (proximo2 < proximo1) {
                Thread.sleep(proximo2);
                System.out.println("Rodrigues");
                proximo1 = proximo2 - proximo1;
                proximo2 = DELAY2;
            }
            else{
                System.out.println("Teste");
            }
        }
    }
}