import pytest
from main import solve_one, solve_two


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            """3   4
4   3
2   5
1   3
3   9
3   3
""",
            11,
        )
    ],
)
def test_problem_one(text, expected):
    assert solve_one(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            """3   4
4   3
2   5
1   3
3   9
3   3
""",
            31,
        )
    ],
)
def test_problem_two(text, expected):
    assert solve_two(text) == expected
