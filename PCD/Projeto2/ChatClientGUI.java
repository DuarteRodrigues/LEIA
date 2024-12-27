/**
 * Starting point for a GUI for a chat application.
 *
 * Programação Concorrente e Ditribuída.
 * 2024/2025
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Simple GUI chat client.
 */
public class ChatClientGUI extends JFrame {
    private JTextArea messageArea;
    private JTextField textField;
    private JButton exitButton;
    private ChatClient client;

    public ChatClientGUI() {
        super("Chat Application");

        /**
         * Set sizes, fonts and colors.
         */
        setSize(400, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        Color backgroundColor = new Color(240, 240, 240);
        Color buttonColor = new Color(75, 75, 75);
        Color textColor = new Color(50, 50, 50);
        Font textFont = new Font("Arial", Font.PLAIN, 14);
        Font buttonFont = new Font("Arial", Font.BOLD, 12);

        /**
         * Create message area.
         */
        messageArea = new JTextArea();
        messageArea.setEditable(false);
        messageArea.setBackground(backgroundColor);
        messageArea.setForeground(textColor);
        messageArea.setFont(textFont);
        JScrollPane scrollPane = new JScrollPane(messageArea);
        add(scrollPane, BorderLayout.CENTER);

        /**
         * Dialog box for entering name.
         */
        String clientName = JOptionPane.showInputDialog(this, "Enter your name:", "Name Entry", JOptionPane.PLAIN_MESSAGE);
        if (clientName == null || clientName.trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "Name cannot be empty", "Error", JOptionPane.ERROR_MESSAGE);
            System.exit(1);
        }
        this.setTitle("Chat Application - " + clientName);
        textField = new JTextField();
        textField.setFont(textFont);
        textField.setForeground(textColor);
        textField.setBackground(backgroundColor);
        textField.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                /*String message = "[" + new SimpleDateFormat("HH:mm:ss").format(new Date()) + "] " + name + ": " + textField.getText();
                client.sendMessage(message);  // Send message
                textField.setText("");*/

                String message = clientName + ": " + textField.getText(); // Include name in message
                client.sendMessage(message);  // Send message to server
                messageArea.append("[" + new SimpleDateFormat("HH:mm:ss").format(new Date()) + "] " + message + "\n");  // Append message to message area with timestamp
                textField.setText("");  // Clear the text field
            }
        });

        /**
         * Exit button.
         */
        exitButton = new JButton("Exit");
        exitButton.setFont(buttonFont);
        exitButton.setBackground(buttonColor);
        exitButton.setForeground(Color.WHITE);
        exitButton.addActionListener(e -> {
            String departureMessage = clientName + " has left the chat.";
            client.sendMessage(departureMessage); // Send "exit" message to participants
            try {
                Thread.sleep(1000);
            } catch (InterruptedException ie) {
                Thread.currentThread().interrupt();
            }
            System.exit(0);
        });

        /**
         * Add text field and exit button to bottom of window.
         */
        JPanel bottomPanel = new JPanel(new BorderLayout());
        bottomPanel.setBackground(backgroundColor);
        bottomPanel.add(textField, BorderLayout.CENTER);
        bottomPanel.add(exitButton, BorderLayout.EAST);
        add(bottomPanel, BorderLayout.SOUTH);

        /**
         * Create ChatClient.
         */
        try {
            this.client = new ChatClient(clientName);
            this.client.connectToServer("127.0.0.1", 5000);
            this.client.setMessageReceivedHandler(this::onMessageReceived);
            client.startMessageSendThread();
        } catch (IOException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this,
                    "Error connecting to the server", "Connection error",
                    JOptionPane.ERROR_MESSAGE);
            System.exit(1);
        }
    }

    private void onMessageReceived(String message) {
        SwingUtilities.invokeLater(() -> messageArea.append(message + "\n"));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new ChatClientGUI().setVisible(true);
        });
    }
}