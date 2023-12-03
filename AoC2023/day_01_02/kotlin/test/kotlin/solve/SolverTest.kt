package solve

import org.junit.Assert
import org.junit.Test
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.CsvSource

class SolverTest {
    @ParameterizedTest
    @CsvSource(
            value =
                    [
                            "two1nine,29",
                            "eightwothree,83",
                            "abcone2threexyz,13",
                            "xtwone3four,24",
                            "4nineeightseven2,42",
                            "zoneight234,14",
                            "7pqrstsixteen,76",
                            "6kvfn,66"]
    )
    fun testSolverCaseExpected(input: String?, expected: String?) {
        Assert.assertEquals(solve.Solver.solve_case(input), expected)
    }

    @Test
    fun testSolver() {
        val utils: solve.Utils = solve.Utils()
        val content: String = utils.getResourceFileAsString("input.txt")
        Assert.assertEquals(solve.Solver.solve(content), "281")
    }
}
