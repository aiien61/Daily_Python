import pytest
from src.module_math import square

@pytest.mark.math
def test_square():
    assert square(8) == 64
