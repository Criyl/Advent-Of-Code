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
        if start + rang < self.src_range_start:
            return False

        # overshot right
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

    # pair(14,55)   self(52,50,5)
    #
    # (14,36) (50,5) (55,11)
    #        |
    #        v
    # (14,36) (52,19) (55,11)
    #    r       a       r
    #
    # [(14,36),(52,19)], (55,11)

    # pair(14,5)   self(52,50,5)
    #
    # (14,5)
    #   |
    #   v
    # (14,5)
    #
    # [(14,5)], None
    def split_pair(self, pair):
        (start, rang) = pair

        #
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
            return [
                (start, self.src_range_start),
                self.convert(
                    (self.src_range_start, start + rang - self.src_range_start)
                ),
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
            second = (first[0], start - first[1])
            return [
                self.convert(first),
            ], (second)
            ...

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

            if found is False:
                converted += [working_pair]

        converted.sort()
        return converted


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
    print(seed_pairs)
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

    # converted_arr = []

    # for seed_pair in seed_pairs:
    #     converted = [seed_pair]
    #     for i in range(len(sequence) - 1):
    #         converted = maps[(sequence[i], sequence[i + 1])].convert(converted)
    #     converted_arr += converted
    # converted_arr.sort()
    # print(f"results: {converted_arr}")

    converted = seed_pairs
    for i in range(len(sequence) - 1):
        converted = maps[(sequence[i], sequence[i + 1])].convert(converted)
        print(f"{sequence[i]} -> {sequence[i + 1]}: {converted}")
    print()
    print(converted)
    return f"{converted[0]}"


if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
        print(solve(text))
