/**
 * ChatClient: Implements ChatClientInterface for client-server communication.
 */

import java.io.*;
import java.net.*;
import java.util.function.Consumer;

public class ChatClient implements ChatClientInterface{
    private Socket socket;
    private PrintWriter out;
    private BufferedReader in;
    private Consumer<String> messageReceivedHandler;
    private String clientName;

    public ChatClient(String clientName){
        this.clientName = clientName;
    }

    @Override
    public void connectToServer(String serverAddress, int serverPort) throws IOException {
        socket = new Socket(serverAddress, serverPort);
        out = new PrintWriter(socket.getOutputStream(), true);
        in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
    }

    @Override
    public void setMessageReceivedHandler(Consumer<String> onMessageReceived) {
        this.messageReceivedHandler = onMessageReceived;
        // Start a thread to listen for incoming messages from the server

        new Thread(() -> {
            try{
                String message;
                while ((message = in.readLine()) != null) {
                    messageReceivedHandler.accept(message);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }).start();
    }

    @Override
    public void sendMessage(String msg) {
        out.println(msg); // Send message to server
    }

    @Override
    public void startMessageSendThread() {
        // Not needed for ChatClientGUI
    }

    public void close() throws IOException {
        out.close();
        in.close();
        socket.close();
    }
}