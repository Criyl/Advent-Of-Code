def isSafe(splitted) -> bool:
    if len(splitted) < 2:
        return False
    current = int(splitted[0])

    direction = 0

    for val in splitted[1:]:
        valAsInt = int(val)
        diff = current - valAsInt

        if direction == 0:
            direction = diff
        elif direction > 0 and diff < 0:
            return False
        elif direction < 0 and diff > 0:
            return False

        if abs(diff) > 3 or diff == 0:
            return False
        current = valAsInt
    return True


def solve(text):
    count = 0
    for line in text.split("\n"):
        splitted = line.split(" ")
        safe = isSafe(splitted)

        if not safe:
            for i, _ in enumerate(splitted):
                alternate = splitted[:i] + splitted[i + 1 :]
                if isSafe(alternate):
                    safe = True
                    break

        if safe:
            count += 1

    return count


if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
        print(solve(text))
