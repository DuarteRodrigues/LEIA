import java.util.Scanner;

public class Homework1{

    public static void main(String[] Args){
        //Declare variables
        int num1 = 5;
        int num2 = 6;
        int sum = num1 + num2;
        int sub = num1 - num2;
        int mul = num1 * num2;
        int div = num1 / num2;
        int rem = num1 % num2;

        Scanner scanner = new Scanner(System.in);

        //2. Print the sum of the numbers declared
        System.out.println("\nThe sum of the numbers is: " + sum);
        
        //Console separators
        System.out.println("\n-----------------------\n");

        //3. Print all prime numbers from 1 to 10
        System.out.println("All prime numbers from 1 to 10: ");
        for (int i=2 ;i<=10 ; i++) {
            if (isPrime(i)){
                System.out.println(i);
            }
        }

        //Console separators
        System.out.println("\n-----------------------\n");

        //4. Print the addition, subtraction, multiplication, division and remainder of any two numbers
        System.out.println("The sum of the numbers is: " + sum);
        System.out.println("The subtraction of the numbers is: " + sub);
        System.out.println("The multiplication of the numbers is: " + mul);
        System.out.println("The division of the numbers is: " + div);
        System.out.println("The remainder of the numbers is: " + rem);

        //Console separators
        System.out.println("\n-----------------------\n");

        //5. Print the multiplication result of a number of the users choosing from 1 to 10
        System.out.println("Insert the number whose table you wish to see:");
        int num = scanner.nextInt();
        System.out.print("\n");
        for (int j=1; j<=10;j++){
            System.out.println(num + " x " + j + " = " + num*j);
        }

        //Console separators
        System.out.println("\n-----------------------\n");

        //6. Print the area and perimeter of a rectangle
        System.out.println("Indicate the height of the rectangle:");
        double h = scanner.nextDouble();
        System.out.println("Indicate the width of the rectangle:");
        double w = scanner.nextDouble();

        System.out.println("The perimeter of the rectangle is: " + (h+h)+(w+w));
        System.out.println("The area of the rectangle is: " + h*w);

    }

    //Function to check if a number is prime
    public static boolean isPrime(int n) {
        if (n<=1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++){
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}