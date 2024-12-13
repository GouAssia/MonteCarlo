import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class WriteFile {
    public static void writeResult(String outputFilePath, int numIterations, double value, long duration, PiMonteCarlo PiVal, int nbProcessor) {
        File file = new File(outputFilePath);
        boolean fileExists = file.exists();

        String resultLine = String.format(
                "%d;%f;%dms;%d;%d;%f\n",
                numIterations,
                value,
                duration,
                nbProcessor,
                PiVal.nAtomSuccess.get(),
                (value - Math.PI) / Math.PI
        );

        try (FileWriter writer = new FileWriter(outputFilePath, true)) {
            if (!fileExists) {
                writer.append("Nombre d'itérations;Pi;Time;nombre de processeur;Nombre de points dans le cercle;Error\n");
            }
            writer.append(resultLine);
        } catch (IOException e) {
            System.err.println("Erreur: " + e.getMessage());
        }
    }
}
