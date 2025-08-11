from unittest.mock import patch, call, MagicMock
from src.module_math import add_random
import pytest


def test_add_random_context_manager():
    with patch("random.randint", return_value=45) as randint:
        assert add_random(5) == 50
    
    assert randint.call_args == call(0, 100)

@patch("random.randint", return_value=45)
def test_add_random_decorator(randint: MagicMock):
    assert add_random(5) == 50
    assert randint.call_args == call(0, 100)

def mock_randint(*args):
    assert args == (0, 100)
    return 45

def test_add_random_monkeymock(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("random.randint", mock_randint)
    assert add_random(5) == 50

def test_add_random_monkeymock_context(monkeypatch: pytest.MonkeyPatch):
    with monkeypatch.context() as m:
        m.setattr("random.randint", mock_randint)
        assert add_random(5) == 50
