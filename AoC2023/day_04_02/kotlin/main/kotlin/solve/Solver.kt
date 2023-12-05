package solve

import java.util.Vector

class Solver {
    companion object {

        fun do_card(text: String): Pair<Int, Int> {
            var points: Int = 0
            var multiplier: Int = 1

            val cardInfo: List<String> = text.split(": ")
            val cardNum: String = cardInfo[0].split(" ")[1]
            val cardContent: List<String> = cardInfo[1].split(" | ")
            val scratches: List<String> = cardContent[0].split(" ")
            val winningNums: List<String> = cardContent[1].split(" ")

            for (num in scratches) {
                if (num in winningNums && num != "") {
                    if (points >= 1) {
                        multiplier *= 2
                    }
                    points++
                }
            }

            if (points > 0) {
                return Pair(multiplier, points)
            }
            return Pair(0, 0)
        }

        @JvmStatic
        fun solve(input: String): String {
            var points: Int = 0
            val cards_multiplier: Vector<Int> = Vector()
            val cards: List<Int> =
                    input.split("\n").map { line ->
                        val (_, card_points) = do_card(line)
                        cards_multiplier.add(1)
                        card_points
                    }

            cards.mapIndexed { i, card_points ->
                for (j in IntRange(1, card_points + 1)) {
                    if (i + j < cards_multiplier.size) {
                        cards_multiplier[i + j] += cards_multiplier[i]
                    }
                }
            }

            println(cards)
            println(cards_multiplier)

            cards_multiplier.map { value -> points += value }

            return input
        }
    }
}
