import json


def cmp(a, b):  # -1 if a < b, 0 if a = b
    if type(a) is int and type(b) is int:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
    elif type(a) is list and type(b) is int:
        b = [b]
    elif type(a) is int and type(b) is list:
        a = [a]

    n = len(a)
    m = len(b)
    for aa, bb in zip(a, b):
        r = cmp(aa, bb)
        if r != 0:
            return r
    if n < m:
        return -1
    elif n == m:
        return 0
    else:
        return 1


def inorder(first, second):
    return cmp(first, second) <= 0


def parseLine(line):
    return json.loads(line)
    ...


if __name__ == "__main__":
    with open("input.txt") as file:
        decoderA = [[2]]
        decoderB = [[6]]
        arr = [decoderA, decoderB]
        count = 0
        i = 1
        while file.readable():
            firstLine = file.readline()
            secondLine = file.readline()
            throwaway = file.readline()
            if firstLine == "" or secondLine == "":
                break
            first = parseLine(firstLine)
            second = parseLine(secondLine)

            arr += [first]
            arr += [second]

            if inorder(first, second):
                count += i
                print(i)
            i += 1
        print(count)

        for n in range(len(arr) - 1):
            for i in range(len(arr) - 1):
                if not inorder(arr[i], arr[i + 1]):
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp

        total = 1
        for i, thing in enumerate(arr):
            if thing == decoderA or thing == decoderB:
                total *= i + 1
            print(thing)
        print(total)
