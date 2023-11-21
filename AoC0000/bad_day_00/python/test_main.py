from main import solve
import pytest


@pytest.mark.parametrize("text, expected", [("Test Case One", "Hello, Place")])
def test_problem(text, expected):
    assert solve(text) == expected
