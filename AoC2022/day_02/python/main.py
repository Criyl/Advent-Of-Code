XYZ_TO_ABC = {"X": "A", "Y": "B", "Z": "C"}

MATCHUP_SCORE = {
    ("A", "A"): 1 + 3,
    ("A", "B"): 2 + 6,
    ("A", "C"): 3 + 0,
    ("B", "A"): 1 + 0,
    ("B", "B"): 2 + 3,
    ("B", "C"): 3 + 6,
    ("C", "A"): 1 + 6,
    ("C", "B"): 2 + 0,
    ("C", "C"): 3 + 3,
}

XYZ_TO_RESULT = {"X": "L", "Y": "D", "Z": "W"}
MATCHUP_VICTORY = {
    ("A", "D"): "A",
    ("A", "W"): "B",
    ("A", "L"): "C",
    ("B", "L"): "A",
    ("B", "D"): "B",
    ("B", "W"): "C",
    ("C", "W"): "A",
    ("C", "L"): "B",
    ("C", "D"): "C",
}

part1 = 0
part2 = 0
with open("input.txt") as file:
    for line in file.readlines():
        if line == "":
            break
        opponent, cheater = line.strip().split(" ")

        part1 += MATCHUP_SCORE[(opponent, XYZ_TO_ABC[cheater])]

        desire = MATCHUP_VICTORY[(opponent, XYZ_TO_RESULT[cheater])]
        part2 += MATCHUP_SCORE[(opponent, desire)]


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")


def part1(file):
    result = 0
    for line in file.readlines():
        if line == "":
            break
        opponent, cheater = line.strip().split(" ")
        result += MATCHUP_SCORE[(opponent, XYZ_TO_ABC[cheater])]
    return result


def part2(file):
    result = 0
    for line in file.readlines():
        if line == "":
            break
        opponent, cheater = line.strip().split(" ")
        MATCHUP_SCORE[(opponent, XYZ_TO_ABC[cheater])]

        desire = MATCHUP_VICTORY[(opponent, XYZ_TO_RESULT[cheater])]
        result += MATCHUP_SCORE[(opponent, desire)]
    return result


with open("input.txt") as file:
    part1(file)
    part2(file)
