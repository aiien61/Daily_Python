from unittest.mock import MagicMock
from src.database import query_db
import pytest

@pytest.fixture
def mock_db_client() -> MagicMock:
    """A fixture that creates a mock database client with a mock cursor."""
    mock_cursor = MagicMock()
    mock_client = MagicMock()
    mock_client.cursor.return_value = mock_cursor
    yield mock_client

def test_query_db_with_mock(mock_db_client: MagicMock):
    # Arrange
    sql_query = "SELECT COUNT(1) FROM example"
    expected_result = (1234,)

    # Get the pre-made mock cursor from the client's configure
    mock_cursor = mock_db_client.cursor.return_value
    mock_cursor.fetchone.return_value = expected_result

    # Act: Run the function with the fake client
    result = query_db(mock_db_client, sql_query)

    # Assert: state-based testing
    assert result == expected_result

    # Assert: behaviour-based testing
    # Assert that the client was used to create a cursor
    mock_db_client.cursor.assert_called_once()
    # Assert that the CURSOR was used correctly
    mock_cursor.execute.assert_called_once_with(sql_query)
    mock_cursor.fetchone.assert_called_once()
    mock_cursor.close.assert_called_once()
