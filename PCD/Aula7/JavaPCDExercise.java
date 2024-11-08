package LEIA.PCD.Aula7;

public class JavaPCDExercise {
    public static void main(String[] args) {
        AnyClass anyClass = new AnyClass();
         
        new Thread() {
            @Override
            public void run() {
                anyClass.anyMethod();
            }
        }.start();
         
        new Thread() {
            @Override
            public void run() {
                anyClass.anyMethod();
            }
        }.start();
         
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
         
        System.out.println(anyClass.s);
    }
}

class AnyClass {
    String s ="1";
     
    synchronized void anyMethod() {
        s = s + s;
    }
}