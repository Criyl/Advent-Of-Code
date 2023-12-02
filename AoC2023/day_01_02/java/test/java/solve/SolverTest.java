package solve;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

public class SolverTest {

  @ParameterizedTest
  @CsvSource({
      "two1nine,29",
      "eightwothree,83",
      "abcone2threexyz,13",
      "xtwone3four,24",
      "4nineeightseven2,42",
      "zoneight234,14",
      "7pqrstsixteen,76",
      "6kvfn,66"
  })
  public void testSolverCaseExpected(String input, String expected) {
    assertEquals(Solver.solve_case(input), expected);
  }

  @Test
  public void testSolver() {
    Utils utils = new Utils();
    String content = utils.getResourceFileAsString("input.txt");
    assertEquals(Solver.solve(content), "281");
  }
}