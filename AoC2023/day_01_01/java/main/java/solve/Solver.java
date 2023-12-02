package solve;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solver {

    public static String solve_case(String input){

        String regex = "([0-9])";
        Pattern pattern = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(input);

        List<String> allMatches = new ArrayList<String>(); 
        while (matcher.find()) {
            allMatches.add(matcher.group());
        }
        return  allMatches.getFirst()+""+allMatches.getLast();
    }

    public static String solve(String input){
        int count = 0;
        for(String line : input.split("\n")){
            count += Integer.parseInt(solve_case(line));
        }
        return ""+count;
    }
}