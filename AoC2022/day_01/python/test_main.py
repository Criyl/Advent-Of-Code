import pytest
from .main import part1, part2


@pytest.mark.parametrize(
    "input, expected",
    [(open("input.txt"), 70296)],
)
def test_part1(input, expected):
    assert part1(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [(open("input.txt"), 205381)],
)
def test_part2(input, expected):
    assert part2(input) == expected
