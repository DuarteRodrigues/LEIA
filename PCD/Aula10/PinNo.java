package LEIA.PCD.Aula10;

import java.io.Serializable;

public class PinNo implements Serializable {

    private final int pin;

    public PinNo(int pin){
        this.pin = pin;
    }

    public int getPin() {
        return pin;
    }
    
}
