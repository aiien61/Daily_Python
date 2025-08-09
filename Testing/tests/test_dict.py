import pytest
from src.module_dict import update_value_by_key, check_key_exists

@pytest.fixture()
def test_dict():
    return {"a": 1, "b": 2}

@pytest.mark.dictionary
def test_update_valye_by_key(test_dict):
    # test_dict: dict = {"a": 1, "b": 2}

    new_dict = update_value_by_key(origin_dict=test_dict, key="b", value=999)

    assert new_dict["b"] == 999

@pytest.mark.dictionary
def test_update_value_by_key_error(test_dict):
    # test_dict: dict = {"a": 1, "b": 2}

    with pytest.raises(KeyError):
        new_dict = update_value_by_key(origin_dict=test_dict, key="error_key", value=999)
    
@pytest.mark.dictionary
def test_check_key_exists(test_dict):
    # test_dict: dict = {"a": 1, "b": 2}

    assert check_key_exists(my_dict=test_dict, key="a")
    assert not check_key_exists(my_dict=test_dict, key="not existed")

