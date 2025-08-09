import pytest
import time
from unittest.mock import patch
from datetime import datetime
from src.module_time import get_current_month, sleep_for_a_while

@pytest.mark.time
def test_get_current_month():
    with patch("src.module_time.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2025, 5, 1, 0, 0, 0)
        month = get_current_month()
        assert month == 5

@pytest.mark.time
def test_sleep_for_a_while_replace():
    # Use patch to replace time.sleep with time.sleep(2)
    with patch("src.module_time.time.sleep", new_callable=time.sleep(1)):
        response = sleep_for_a_while(20)
        assert response == 20

@pytest.mark.time
def test_sleep_for_a_while_mock():
    # Use patch to replace time.sleep() with None
    with patch("src.module_time.time.sleep"):
        response = sleep_for_a_while(20)
        assert response == 20
