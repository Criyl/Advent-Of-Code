import pytest
from main import solve


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
def test_problem(text, expected):
    assert solve(text) == expected
