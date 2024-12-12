package LEIA.PCD.Aula10;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface BankAccount extends Remote {
    String showBalance(AccountID id, PinNo pin) throws RemeteException;
}