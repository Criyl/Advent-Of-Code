import re
from dataclasses import dataclass
import math


@dataclass
class NumberSet:
    value: int
    row: int
    col: int

    def size(self):
        if self.value == 0:
            return 1

        count = 1
        temp = self.value
        while temp >= 10:
            count += 1
            temp /= 10
        return count

    def touching(self, position):
        def distance(pos1, pos2):
            dx = abs(pos1[0] - pos2[0])
            dy = abs(pos1[1] - pos2[1])
            return math.sqrt(dx**2 + dy**2)

        min_dist = 999999
        for i in range(self.col, self.col + self.size()):
            dis = distance((self.row, i), position)
            if dis < min_dist:
                min_dist = dis
        return min_dist < 2


def ingest_numbers(text):
    arr = []
    row = 0
    regex = re.compile("[0-9]+")
    for line in text.split("\n"):
        subline = line
        search = regex.search(subline)
        following = 0
        while search:
            col = search.span()[0] + following
            following += search.span()[1]

            thing = NumberSet(int(search.group()), row, col)

            arr += [thing]
            subline = subline[search.span()[1] :]

            search = regex.search(subline)
        row += 1
    return arr


def ingest_characters(text):
    arr = []
    row = 0
    regex = re.compile("[^.|0-9]")
    for line in text.split("\n"):
        subline = line
        search = regex.search(subline)
        following = 0
        while search:
            col = search.span()[0] + following
            following += search.span()[1]

            pos = (row, col)
            arr += [pos]
            subline = subline[search.span()[1] :]
            search = regex.search(subline)
        row += 1
    return arr


def solve(text):
    numbers = ingest_numbers(text)
    specials = ingest_characters(text)
    sum = 0
    for number in numbers:
        touching = False
        for special in specials:
            if number.touching(special):
                touching = True

        if touching:
            sum += number.value

    return sum


if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
        print(solve(text))
