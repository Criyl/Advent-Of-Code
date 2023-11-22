highest = 0
arr = [0]
with open("input.txt") as file:
    count = 0
    for line in file.readlines():
        stripped = line.strip()
        if stripped == "":
            highest = max(count, highest)
            arr += [count]
            count = 0
        else:
            num = int(line.strip())
            count += num

print(f"Highest: {highest}")
sumTopThree = sum(sorted(arr, reverse=True)[:3])
print(f"Top Sum: {sumTopThree}")


def part1(file):
    highest = 0
    arr = [0]
    with open("input.txt") as file:
        count = 0
        for line in file.readlines():
            stripped = line.strip()
            if stripped == "":
                highest = max(count, highest)
                arr += [count]
                count = 0
            else:
                num = int(line.strip())
                count += num
    return highest


def part2(file):
    highest = 0
    arr = [0]
    with open("input.txt") as file:
        count = 0
        for line in file.readlines():
            stripped = line.strip()
            if stripped == "":
                highest = max(count, highest)
                arr += [count]
                count = 0
            else:
                num = int(line.strip())
                count += num

    sumTopThree = sum(sorted(arr, reverse=True)[:3])
    return sumTopThree
