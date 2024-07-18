package extension.libs;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class IO {

    public static String openFile(String filePath) {
        try {
            return new String(Files.readAllBytes(Paths.get(filePath)));
        } catch (IOException e) {
            e.printStackTrace();
            return "";
        }
    }

    public static void createFile(String name, String text) {
        try {
            Files.write(Paths.get(name), text.getBytes(), StandardOpenOption.CREATE);
            System.out.println("Archivo creado: " + name);
        } catch (IOException e) {
            System.err.println("Error al crear el archivo: " + e.getMessage());
        }
    }
}
