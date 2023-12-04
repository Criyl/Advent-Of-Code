import re
from dataclasses import dataclass
import math

# No peeking


def do_card(text):
    points = 0
    multiplier = 1

    cardInfo = text.split(": ")
    cardNum = cardInfo[0].split(" ")[1]
    cardContent = cardInfo[1].split(" | ")
    scratches = cardContent[0].split(" ")
    winningNums = cardContent[1].split(" ")

    for num in scratches:
        if num in winningNums and num != "":
            if points >= 1:
                multiplier *= 2
            points += 1
    if points > 0:
        return multiplier, points
    else:
        return 0, 0


def solve(text):
    points = 0
    cards = []
    cards_multi = []

    for line in text.split("\n"):
        _, card_points = do_card(line)
        cards += [card_points]

    for _ in cards:
        cards_multi += [1]

    for i, card in enumerate(cards):
        for j in range(1, card + 1):
            cards_multi[i + j] += cards_multi[i]

    for i, card in enumerate(cards):
        points += cards_multi[i]
    return f"{points}"


if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
        print(solve(text))
