import java.io.IOException;
import java.util.function.Consumer;

public interface ChatClientInterface {

    public void connectToServer(String serverAddress, int serverPort) throws IOException;
    public void setMessageReceivedHandler(Consumer<String> onMessageReceived);
    public void sendMessage(String msg);
    public void startMessageSendThread();
}
