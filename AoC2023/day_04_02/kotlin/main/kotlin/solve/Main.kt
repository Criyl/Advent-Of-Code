package solve

fun main() {
    val utils: Utils = Utils()
    val content = utils.getResourceFileAsString("input.txt")
    System.out.println(Solver.solve(content))
}
