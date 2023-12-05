package solve

import kotlin.test.Test
import kotlin.test.assertEquals

internal class SolverTest {

    @Test
    fun testHelloWorld() {
        val utils: Utils = Utils()
        val content = utils.getResourceFileAsString("input.txt")
        assertEquals(Solver.solve(content), "30")
    }
}
