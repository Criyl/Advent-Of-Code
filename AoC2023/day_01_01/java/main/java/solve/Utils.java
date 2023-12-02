package solve;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.nio.charset.StandardCharsets;

public class Utils {
    public String getResourceFileAsString(String fileName) {
        InputStream inputStream = getClass().getClassLoader().getResourceAsStream(fileName);

        StringBuilder textBuilder = new StringBuilder();

        try (
        Reader reader = new BufferedReader(
            new InputStreamReader(inputStream, StandardCharsets.UTF_8)
            )
        ) {
            int c = 0;
            while ((c = reader.read()) != -1) {
                textBuilder.append((char) c);
            }
        }catch(Exception e){
            System.err.println(e);
        }
        return textBuilder.toString();
    }
}
