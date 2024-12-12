package LEIA.PCD.Aula10;

import java.io.Serializable;

public class AccountID implements Serializable {

    private final int accountNumber;

    public AccountID(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public int getAccountNumber() {
        return accountNumber;
    }
}
