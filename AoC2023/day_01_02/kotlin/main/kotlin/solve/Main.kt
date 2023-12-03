package solve

fun main() {
    val utils = Utils()
    val content = utils.getResourceFileAsString("input.txt")
    println(Solver.solve(content))
}
