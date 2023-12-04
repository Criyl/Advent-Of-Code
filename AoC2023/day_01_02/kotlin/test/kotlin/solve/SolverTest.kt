package solve

import kotlin.test.Test
import kotlin.test.assertEquals
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
    fun testSolverCaseExpected(input: String, expected: String) {
        assertEquals(Solver.solve_case(input), expected)
    }

    @Test
    fun testSolver() {
        val utils: Utils = Utils()
        val content: String = utils.getResourceFileAsString("input.txt")
        assertEquals(Solver.solve(content), "281")
    }
}
