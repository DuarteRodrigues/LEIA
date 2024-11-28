// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// Java Serialization: Ex1

package LEIA.PCD.Aula8;


import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.Date;

public class Ex1 {
    public static void main(String[] args) {
        // Create a serializable object
        String operation = "serialize"; // Change to "deserializable" for the other operation

        if (operation.equals("serialize")){
            PersistentTime persistentTime = new PersistentTime("Example string");
            SerializeTime.serialize(persistentTime);
        } else if (operation.equals("deserialize")) {
            PersistentTime persistentTime = DeserializeTime.deserialize();
            if (persistentTime != null) {
                System.out.println("Time: " + persistentTime.getTime());
                System.out.println("Something: " + persistentTime.getSomething());
            }
        } else {
            System.out.println("Invalid operation");
        }
    }
}

// Class representing the serializable object
class PersistentTime implements Serializable{
    private static final long serialVersionUID = 1L; // For serialization version control
    private final Date time;
    private final transient String something; // When an instance variable is declared as transient, it will not be serialized.
    // Whatever value it holds won't be stored in the output file, resulting in a 'null' or the  standard value of the primitive type where the value should be when the variable is deserialized

    public PersistentTime(String something){
        this.something = something;
        this.time = new Date(); // Initializes with actual date and time
    }

    public Date getTime(){
        return time;
    }

    public String getSomething(){
        return something;
    }
}

// Class to handle serialization of a PersistentTime object
class SerializeTime {
    public static void serialize(PersistentTime persistentTime) {
        String fileName = "persistentTime.ser"; // File name for serialization

        try(FileOutputStream fileOut = new FileOutputStream(fileName);
        ObjectOutputStream out = new ObjectOutputStream(fileOut)) {
            out.writeObject(persistentTime);
            System.out.println("Dados serializados estão guardados em " + fileName);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

// Class to handle deserialization for a PersistentTime object
class DeserializeTime {
    public static PersistentTime deserialize() {
        String fileName = "persistentTime.ser"; // File name for deserialization

        try (FileInputStream fileIn = new FileInputStream(fileName);
        ObjectInputStream in = new ObjectInputStream(fileIn)){
            PersistentTime persistentTime = (PersistentTime) in.readObject();
            System.out.println("Object deserialized!");
            return persistentTime;
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }
}
