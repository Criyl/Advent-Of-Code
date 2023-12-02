package solve;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solver {

    public static String solve_case(String input) {

        String regex = "([0-9])";

        Matcher first = Pattern.compile(regex + ".*").matcher(input);
        Matcher last = Pattern.compile(".*" + regex).matcher(input);

        first.find();
        last.find();

        String firstValue = first.group(1);
        String lastValue = last.group(1);

        return "" + firstValue + "" + lastValue;
    }

    public static String solve(String input) {
        int count = 0;
        for (String line : input.split("\n")) {
            count += Integer.parseInt(solve_case(line));
        }
        return "" + count;
    }
}