package solve

import java.io.BufferedReader
import java.io.InputStreamReader
import java.nio.charset.StandardCharsets

class Utils {
    init {}

    fun getResourceFileAsString(fileName: String?): String {
        val inputStream = javaClass.classLoader.getResourceAsStream(fileName)
        val textBuilder = StringBuilder()
        try {
            BufferedReader(InputStreamReader(inputStream, StandardCharsets.UTF_8)).use { reader ->
                var c = 0
                while (reader.read().also { c = it } != -1) {
                    textBuilder.append(c.toChar())
                }
            }
        } catch (e: Exception) {
            System.err.println(e)
        }
        return textBuilder.toString()
    }
}
