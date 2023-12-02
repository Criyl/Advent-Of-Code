package solve;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

public class SolverTest {

  @Test
  public void testSolver() {
    Utils utils = new Utils();
    String content = utils.getResourceFileAsString("input.txt");
    assertEquals(Solver.solve(content), "2286");
  }
}