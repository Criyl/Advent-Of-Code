package solve;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solver {
    static int RED = 12;
    static int BLUE = 14;
    static int GREEN = 13;

    public static String solve_case(String input) {
        String[] splits = input.split(": ");

        String gametext = splits[0];
        String therest = splits[1];

        int red_count = 0;
        int blue_count = 0;
        int green_count = 0;

        for (String set : therest.split("; ")) {
            for (String cube : set.split(", ")) {
                String[] parts = cube.split(" ");

                int value = Integer.parseInt(parts[0].strip());
                String color = parts[1].strip();

                if (color.matches("red")) {
                    red_count = Math.max(red_count, value);
                } else if (color.matches("blue")) {
                    blue_count = Math.max(blue_count, value);
                } else if (color.matches("green")) {
                    green_count = Math.max(green_count, value);
                }
            }
        }

        if (red_count > RED || blue_count > BLUE || green_count > GREEN) {
            return "0";
        }

        return gametext.substring(5);
    }

    public static String solve(String input) {
        int count = 0;
        for (String line : input.split("\n")) {
            int thing = Integer.parseInt(solve_case(line));
            count += thing;
        }
        return "" + count;
    }
}