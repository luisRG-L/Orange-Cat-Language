package extension;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.JOptionPane;

import extension.libs.IO;
import extension.parser.Parser;

public class Init extends JFrame {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new Init());
    }

    public Init () {
        setTitle("ODOC Compiler");
        setLayout(null);
        setExtendedState(MAXIMIZED_BOTH);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        JTextField fileOpener = new JTextField();
        fileOpener.setBounds(10, 50, 600, 20);
        add(fileOpener);

        JTextField outputFile = new JTextField("");
        outputFile.setBounds(10, 80, 600, 20);
        add(outputFile);

        JButton button = new JButton("Compilar");
        button.setBounds(10, 110, 600, 60);
        button.addActionListener(e -> {
            Parser.parse(IO.openFile("docs/"+fileOpener.getText()+".odoc"), outputFile.getText());
            JOptionPane.showMessageDialog(this, "Compilado correctamente");
            System.exit(0);
        });
        add(button);
        setVisible(true);
    }

    @Override
    public String toString() {
        return "Init []";
    }
}
