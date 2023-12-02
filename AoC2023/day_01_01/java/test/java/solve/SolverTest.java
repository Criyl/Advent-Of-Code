package solve;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SolverTest {

  @Test
  public void testSolverCase() {

    String first = "1abc2";
    assertEquals( Solver.solve_case(first), "12");

    String second = "pqr3stu8vwx";
    assertEquals( Solver.solve_case(second), "38");

    String third = "a1b2c3d4e5f";
    assertEquals( Solver.solve_case(third), "15");

    String fourth = "treb7uchet";
    assertEquals( Solver.solve_case(fourth), "77");
  }

  @Test
  public void testSolver() {
    Utils utils = new Utils();
    String content = utils.getResourceFileAsString("input.txt");
    assertEquals( Solver.solve(content), "142");
  }
}