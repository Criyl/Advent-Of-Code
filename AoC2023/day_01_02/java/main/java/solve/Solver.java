package solve;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solver {

    public static String wordToNumber(String wordnumber) {
        if (Pattern.compile("[0-9]").matcher(wordnumber).find()) {
            return wordnumber;
        }
        switch (wordnumber) {
            case "zero":
                return "0";
            case "one":
                return "1";
            case "two":
                return "2";
            case "three":
                return "3";
            case "four":
                return "4";
            case "five":
                return "5";
            case "six":
                return "6";
            case "seven":
                return "7";
            case "eight":
                return "8";
            case "nine":
                return "9";
        }
        return "BADBADBAD";
    }

    public static String solve_case(String input) {

        String regex = "([0-9]|zero|one|two|three|four|five|six|seven|eight|nine)";

        Matcher first = Pattern.compile(regex + ".*").matcher(input);
        Matcher last = Pattern.compile(".*" + regex).matcher(input);

        first.find();
        last.find();

        String firstValue = first.group(1);
        String lastValue = last.group(1);

        return wordToNumber(firstValue) + "" + wordToNumber(lastValue);
    }

    public static String solve(String input) {
        int count = 0;
        for (String line : input.split("\n")) {
            Integer value = Integer.parseInt(solve_case(line));
            count += value;
        }
        return "" + count;
    }
}