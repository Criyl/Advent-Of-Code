package solve;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

public class SolverTest {

  @ParameterizedTest
  @ValueSource(strings = {
      "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
      "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
      "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
  })
  public void testSolverCaseExpectedTrue(String input) {
    assertEquals(Solver.solve_case(input), input.substring(5, 6));
  }

  @ParameterizedTest
  @ValueSource(strings = { "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
      "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
      "Game 3: 7 red, 10 green, 4 blue; 2 blue, 3 green, 5 red; 9 red, 7 green, 3 blue; 3 blue, 6 green, 18 red",
      "Game 4: 1 blue, 2 green, 5 red; 10 red, 1 blue, 3 green; 14 red"
  })

  public void testSolverCaseExpectedFalse(String input) {
    assertEquals(Solver.solve_case(input), "0");
  }

  @Test
  public void testSolver() {
    Utils utils = new Utils();
    String content = utils.getResourceFileAsString("input.txt");
    assertEquals(Solver.solve(content), "8");
  }
}