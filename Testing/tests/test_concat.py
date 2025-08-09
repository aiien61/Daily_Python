import pytest
from src.module_string import concat

@pytest.mark.string
def test_concat():
    str1 = "Kiwi"
    str2 = "noodles"
    assert concat(str1, str2) == "Kiwi noodles"

@pytest.mark.string
def test_concat_failed():
    str1 = 55
    str2 = 66
    with pytest.raises(TypeError):
        concat(str1, str2)
    