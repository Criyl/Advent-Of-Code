from dataclasses import dataclass
from typing import List
import re


# No peeking
@dataclass
class SpecialMapEntry:
    dest_range_start: int
    src_range_start: int
    range_length: int

    def encasing(self, value_pair):
        (start, rang) = value_pair
        if (
            self.src_range_start <= start
            and start + rang <= self.src_range_start + self.range_length
        ):
            return True
        return False

    def valid(self, value_pair):
        # do they not overlap?
        (start, rang) = value_pair

        # overshot left 
        #  0123456789
        #  -----====- entry (5,4)
        #  -====----- pair  (1,4)
        if start + rang <= self.src_range_start:
            return False

        # overshot right
        #  0123456789
        #  -====----- entry (1,4)
        #  -----====- pair  (5,4)
        if self.src_range_start + self.range_length <= start:
            return False
        
        return True

    def convert(self, value_pair):
        (start, rang) = value_pair

        if self.encasing(value_pair):
            diff = start - self.src_range_start
            return (self.dest_range_start + diff, rang)
        else:
            print("BADBADBAD")

        return value_pair

    def split_pair(self, pair):
        (start, rang) = pair

        #  0123456789
        #  ----====-- entry
        #  -----==--- pair
        #
        #  ----====-- entry
        #  ----====-- pair
        #
        if self.encasing(pair):
            return [self.convert(pair)], None

        #  0123456789
        #  ----====-- entry (4,4)
        #  ---====--- pair  (3,4)
        #
        #  ---*===---- (3,1) (4,3)
        #
        elif (
            start <= self.src_range_start
            and start + rang < self.src_range_start + self.range_length
        ):
            first = (start, self.src_range_start - start)
            second = (first[0] + first[1], start + rang - (first[0] + first[1]))

            return [
                first,
                self.convert(second),
            ], None

        #  0123456789
        #  ---=====-- entry (3,5)
        #  -----====- pair  (5,4)
        #
        #  -----===*- (5=5,3+5-5=3) (=8,=1)
        #
        elif (
            self.src_range_start <= start
            and self.src_range_start + self.range_length < start + rang
        ):
            first = (start, self.src_range_start + self.range_length - start)
            second = (first[0]+first[1], rang - first[1])
            return [
                self.convert(first),
            ], (second)

        #  0123456789
        #  ----====-- entry (4,4)
        #  ---======- pair  (3,6)
        #
        #  ---*====*- (3,4-3=1)(4,4)(4+4=8,6-1-4=1)
        #
        else:
            first = (start, self.src_range_start - start)
            second = (self.src_range_start, self.range_length)
            third = (
                self.src_range_start + self.range_length,
                rang - first[1] - second[1],
            )
            return [
                first,
                self.convert(second),
            ], (third)

@dataclass
class SpecialMap:
    src: str
    dest: str
    entries: List[SpecialMapEntry]

    def convert(self, value_pairs):
        converted = []
        working_pairs = value_pairs
        while working_pairs is not None and len(working_pairs) > 0:
            working_pair = working_pairs[0]
            working_pairs = working_pairs[1:] + []
            found = False
            for entry in self.entries:
                if entry.valid(working_pair):
                    found = True
                    results, remainder = entry.split_pair(working_pair)
                    converted += results

                    if (
                        remainder is not None
                        and remainder[0] is working_pair[0]
                        and remainder[1] is working_pair[1]
                    ):
                        converted += [remainder]
                    elif remainder is not None:
                        working_pairs = [remainder] + working_pairs

                    break
            if found is False:
                converted += [working_pair]

        converted.sort()
        converted = eliminate_overlap(converted)
        return converted



def overlap_pairs(pairA, pairB):
    (startA, lenA) = pairA
    (startB, lenB) = pairB

    # A < B
    if pairB[0] < pairA[0]:
        (startA, lenA) = pairB
        (startB, lenB) = pairA

    #  0123456789
    #  ----====-- a
    #  -----==--- b
    #
    #  ----====-- a
    #  ----====-- b
    #
    if (
        startA <= startB
        and  startB + lenB <= startA + lenA 
    ):
        return pairA

    #  0123456789
    #  ---=====-- a (3,5)
    #  -----====- b  (5,4)
    #
    #  ---======- (3,6)
    #
    elif (
        startA < startB
        and startA + lenA <= startB + lenB
    ):
        return (startA, startB + lenB - startA)
    
    #  0123456789
    #  -====----- a (3,5)
    #  ------===- b  (5,4)
    #
    #  None
    #
    else:
        return None

def eliminate_overlap(sorted_pairs):
    stack = sorted_pairs
    collapsed = []

    while stack != []:
        popped = stack[0]
        stack = stack[1:] + []

        focus = 0
        while focus < len(stack) and stack[focus][0] <= popped[0] + popped[1]:
            popped = overlap_pairs(popped, stack[focus])
            focus += 1
        collapsed += [popped]
        stack = stack[focus:]

    return collapsed


def ingest(section):
    header_regex = re.compile("(.*)-to-(.*) map:")
    match = header_regex.search(section)
    header_groups = match.groups()

    entry_regex = re.compile("(.*) (.*) (.*)")
    entry_matches = entry_regex.findall(section)

    entries = []
    for entry in entry_matches:
        e = SpecialMapEntry(int(entry[0]), int(entry[1]), int(entry[2]))
        entries += [e]

    entries = sorted(entries, key=lambda k: k.src_range_start)

    return SpecialMap(src=header_groups[0], dest=header_groups[1], entries=entries)


def build_maps(sections):
    maps = {}

    for section in sections:
        smap = ingest(section)
        maps[(smap.src, smap.dest)] = smap

    return maps


def seed_to_range_pairs(seeds):
    result = []
    for i in range(int(len(seeds) / 2)):
        result += [(int(seeds[2 * i]), int(seeds[2 * i + 1]))]
    result.sort()
    return result


def solve(text):
    seeds = []

    sections = text.split("\n\n")
    seeds = sections[0].split(" ")[1:]
    seed_pairs = seed_to_range_pairs(seeds)
    maps = build_maps(sections[1:])

    sequence = [
        "seed",
        "soil",
        "fertilizer",
        "water",
        "light",
        "temperature",
        "humidity",
        "location",
    ]

    converted = seed_pairs
    for i in range(len(sequence) - 1):
        converted = maps[(sequence[i], sequence[i + 1])].convert(converted)
    return f"{converted[0][0]}"


if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
        print(solve(text))
