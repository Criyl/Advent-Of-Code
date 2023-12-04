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
        return multiplier
    else:
        return 0
    return points * multiplier


def solve(text):
    points = 0
    for line in text.split("\n"):
        card_points = do_card(line)
        points += card_points
    return f"{points}"


if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
        print(solve(text))
