from unittest import mock
from pytest_mock import MockFixture
from src.module_math import check_response_greater_than_0_5
import pytest

@pytest.mark.api
def test_check_response_greater_than_0_5_true():
    with mock.patch("src.module_math.call_external_api") as mock_api_1:
        mock_api_1.return_value = {"response_value": 0.95}
        result = check_response_greater_than_0_5()
        assert result is True

@pytest.mark.api
def test_check_response_greater_than_0_5_false(mocker: MockFixture):
    mock_api_2 = mocker.patch("src.module_math.call_external_api", return_value={"response_value": 0.25})
    result = check_response_greater_than_0_5()
    assert result is False

@pytest.mark.api
def test_check_response_greater_than_0_5_error(mocker: MockFixture):
    mocker_api_3 = mocker.patch("src.module_math.call_external_api", return_value={})
    with pytest.raises(KeyError):
        result = check_response_greater_than_0_5()
