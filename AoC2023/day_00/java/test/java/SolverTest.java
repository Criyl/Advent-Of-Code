package solve;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import solve.Solver;

public class SolverTest {
  @Test
  public void testSolver() {
    assertEquals( Solver.solve("Test Case"), "Hello, World");
  }
}