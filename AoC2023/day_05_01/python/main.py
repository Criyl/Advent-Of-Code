from dataclasses import dataclass
from typing import List
import re


# No peeking
@dataclass
class SpecialMapEntry:
    dest_range_start: int
    src_range_start: int
    range_length: int

    def valid(self, value):
        if (
            self.src_range_start <= value
            and value < self.src_range_start + self.range_length
        ):
            return True
        return False

    def convert(self, value):
        diff = value - self.src_range_start
        return self.dest_range_start + diff


@dataclass
class SpecialMap:
    src: str
    dest: str
    entries: List[SpecialMapEntry]

    def convert(self, value):
        for entry in self.entries:
            if entry.valid(value):
                return entry.convert(value)
        return value


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


def solve(text):
    seeds = []

    sections = text.split("\n\n")
    seeds = sections[0].split(" ")[1:]

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

    converted_arr = []

    for seed in seeds:
        converted = int(seed)

        history = [seed]
        for i in range(len(sequence) - 1):
            converted = maps[(sequence[i], sequence[i + 1])].convert(converted)
            history += [converted]
        converted_arr += [converted]
        print(history)
    converted_arr.sort()
    return f"{converted_arr[0]}"


if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
        print(solve(text))
