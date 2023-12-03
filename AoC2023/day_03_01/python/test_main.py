import pytest
from main import solve


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""",
            4361,
        )
    ],
)
def test_problem(text, expected):
    assert solve(text) == expected
