package solve;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import solve.Solver;

public class SolverTest {
  @Test
  public void testSolver() {
    Utils utils = new Utils();
    String content = utils.getResourceFileAsString("input.txt");
    assertEquals(Solver.solve(content), "Hello, World");
  }
}