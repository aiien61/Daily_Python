from unittest.mock import patch, MagicMock
import pytest
import src.mod2 as mod2
from src.mod1 import preamble

CORRECT_PATCH_TARGET: str = "src.mod2.mod1.preamble"

def test_summer_a():
    with patch(CORRECT_PATCH_TARGET, return_value=""):
        assert mod2.summer(5, 6) == "11"

def test_summer_b():
    with patch(CORRECT_PATCH_TARGET) as mock_preamble:
        mock_preamble.return_value = ""
        assert mod2.summer(5, 6) == "11"

@patch(CORRECT_PATCH_TARGET, return_value="")
def test_summer_c(mock_preamble: MagicMock):
    assert mod2.summer(5, 6) == "11"

@patch(CORRECT_PATCH_TARGET)
def test_summer_d(mock_preamble: MagicMock):
    mock_preamble.return_value = ""
    assert mod2.summer(5, 6) == "11"

def mock_preamble_replacement(*args):
    return ""

def test_summer_monkeymock(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(mod2.mod1, "preamble", mock_preamble_replacement)
    assert mod2.summer(5, 6) == "11"
