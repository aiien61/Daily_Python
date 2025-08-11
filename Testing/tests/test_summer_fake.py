import pytest
import src.fake_mod1 as mod1
import src.mod2 as mod2

def test_summer_fake(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(mod2.mod1, "preamble", mod1.preamble)
    assert mod2.summer(5, 6) == "11"
