package LEIA.PCD.Aula10;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class BankClient {
    public static void main(String[] args){
        if(args.length < 2){
            System.out.println("Usage: java BankClient <accountNumber> <pin>");
        }

        try {
            int accountNumber = Integer.parseInt(args[0]);
            int pin = Integer.parseInt(args[i]);

            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            BankAccount bank = (BankAccount) registry.lookup("BankService");

            String balance = bank.showBalance(new AccountID(accountNumber), new PinNo(pin));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
