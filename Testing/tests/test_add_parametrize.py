from src.module_math import add
import pytest


class TestAdd:
    @pytest.mark.parametrize(
        ("a", "b", "c"),
        [
            (1, 2, 3),
            (3, 5, 8),
            (5, 8, 13),
            (8, 13, 21),
            (13, 21, 34),
            (21, 34, 55),
            (34, 55, 89),
            (55, 89, 144)
        ]
    )
    def test_add(self, a, b, c):
        assert add(a, b) == c