/**
 * ChatServer: Manages client connections and broadcasts messages.
 */

import java.io.*;
import java.net.*;
import java.text.SimpleDateFormat;
import java.util.*;

 public class ChatServer{
    private static final int PORT = 5000;
    private static Set<PrintWriter> clientWriters = new HashSet<>();
    private static Set<String> clientNames = new HashSet<>();

    public static void main (String[] args){
        System.out.println("Chat Server started on port " + PORT);
        try(ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                new ClientHandler(serverSocket.accept()).start();
            }
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    private static class ClientHandler extends Thread {
        private Socket socket;
        private PrintWriter out;
        private BufferedReader in;
        private String clientName;

        public ClientHandler(Socket socket){
            this.socket = socket;
        }

        @Override
        public void run(){
            try{
                // Create input and output streams for the client
                in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                out = new PrintWriter(socket.getOutputStream(), true);

                // Get client name
                clientName = in.readLine();
        
                // Add client to lists
                synchronized (clientWriters) {
                    clientWriters.add(out);
                    clientNames.add(clientName);
                }

                // Notify all clients about the new user
                broadcastMessage("[" + new SimpleDateFormat("HH:mm:ss").format(new Date()) + "] " + clientName + " has entered the chat.");

                // Read and forward messages from the client
                String message;
                while((message = in.readLine()) != null){
                    broadcastMessage(message);
                }
            
            } catch (IOException e){
                e.printStackTrace();
            } finally {
                try {
                    // Clean up and notify all clients
                    if (clientName != null) {
                        synchronized (clientWriters) {
                            clientWriters.remove(out);
                            clientNames.remove(clientName);
                        }
                        broadcastMessage("[" + new SimpleDateFormat("HH:mm:ss").format(new Date()) + "] " + clientName + " has left the chat.");
                    }
                    if (socket != null) {
                        socket.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        private void broadcastMessage(String message) {
            // Add timestamp to the incoming message
            String timestampedMessage = message;

            // Broadcast the message to all connected clients
            synchronized (clientWriters) {
                for (PrintWriter writer : clientWriters) {
                    writer.println(timestampedMessage);  // Send message with timestamp
                }
            }
        }
    }
}