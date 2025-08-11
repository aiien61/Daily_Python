from unittest import TestCase
from unittest.mock import patch
import os
import pytest

class TestEnviron(TestCase):
    def setUp(self):
        os.environ["SAMPLE"] = "foo"

    def tearDown(self):
        try:
            del os.environ["SAMPLE"]
        except KeyError as e:
            print(e)
    
    def test_getenv_success(self):
        actual: str = os.getenv("SAMPLE")
        expected: str = "foo"
        self.assertEqual(actual, expected)
    
    def test_getenv_failure(self):
        actual = os.getenv("NO_THIS_ENVVAR")
        expected = None
        self.assertEqual(actual, expected)

def test_getenv_context():
    with patch.dict("os.environ", {"EXAMPLE": "HELLO, WORLD!"}):
        assert os.getenv("EXAMPLE") == "HELLO, WORLD!"

def test_getenv_monkeymock(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("EXAMPLE", "HELLO, WORLD!")
    assert os.getenv("EXAMPLE") == "HELLO, WORLD!"
