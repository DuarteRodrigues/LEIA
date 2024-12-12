package LEIA.PCD.Aula10;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class BankAccountImpl extends UnicastRemoteObject implements BankAccount {

    private final Map<Integer, AccountData> accounts = new HashMap<>();

    public BankAccountImpl() throws RemoteException{
        super();
        initializeAccounts();
    }

    private void initializeAccounts(){
        Random random = new Random();
        for (int i = 1; i <= 100; i++){
            int pin = 1000 + random.nextInt(9000);
            double balance = 1000 + random.nextDouble() * 6500;
            accounts.put(i, new AccountData(pin, balance));
        }
    }

    @Override
    public String showBalance(AccountID id, PinNo pin) throws RemoteException {
        AccountData account = accounts.get(id.getAccountNumber());
        if (account == null) {
            return "Account not found.";
        }
        if (account.getPin() != pin.getPin()) {
            return "Invalid PIN.";
        }
        return String.format("Balance: %.2f€", account.getBalance());
    }

    private static class AccountData {
        private final int pin;
        private final double balance;

        public AccountData(int pin, double balance) {
            this.pin = pin;
            this.balance = balance;
        }

        public int getPin(){
            return pin;
        }

        public double getBalance(){
            return balance;
        }
    }
}
