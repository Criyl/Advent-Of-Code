package solve

class Solver {
    companion object {
        @JvmStatic
        fun solve(input: String): String {
            val utils: Utils = Utils()
            val content = utils.getResourceFileAsString("input.txt")
            return content
        }
    }
}
