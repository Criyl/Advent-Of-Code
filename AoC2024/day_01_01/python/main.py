def constructLists(text):
    lists = []

    text = text.replace("   ", " ")
    for j, line in enumerate(text.split("\n")):
        for k, number in enumerate(line.split(" ")):
            if number == "":
                continue

            if len(lists) <= k:
                lists += [[int(number)]]
            else:
                lists[k] += [int(number)]

    for i, collection in enumerate(lists):
        lists[i] = sorted(collection)
    return lists


def solve(text):
    lists = constructLists(text)

    for i, collection in enumerate(lists):
        lists[i] = sorted(collection)

    sum = 0
    for i in range(len(lists[0])):
        sum += abs(lists[1][i] - lists[0][i])

    return sum


if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
        print(solve(text))
