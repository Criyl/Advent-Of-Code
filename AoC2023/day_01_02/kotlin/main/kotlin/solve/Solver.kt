package solve

import java.util.regex.Pattern

class Solver {
    companion object {
        fun wordToNumber(wordnumber: String): String {
            if (Pattern.compile("[0-9]").matcher(wordnumber).find()) {
                return wordnumber
            }
            when (wordnumber) {
                "zero" -> return "0"
                "one" -> return "1"
                "two" -> return "2"
                "three" -> return "3"
                "four" -> return "4"
                "five" -> return "5"
                "six" -> return "6"
                "seven" -> return "7"
                "eight" -> return "8"
                "nine" -> return "9"
            }
            return "BADBADBAD"
        }

        fun solve_case(input: String): String {
            val regex = "([0-9]|zero|one|two|three|four|five|six|seven|eight|nine)"
            val first = Pattern.compile("$regex.*").matcher(input)
            val last = Pattern.compile(".*$regex").matcher(input)
            first.find()
            last.find()
            val firstValue = first.group(1)
            val lastValue = last.group(1)
            return wordToNumber(firstValue) + "" + wordToNumber(lastValue)
        }

        fun solve(input: String): String {
            var count = 0
            for (line in input!!.split("\n").toTypedArray()) {
                val value = solve_case(line).toInt()
                count += value
            }
            return "" + count
        }
    }
}
