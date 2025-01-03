import pytest
from sqlalchemy import create_engine
from decouple import config


@pytest.fixture
def database_url():
    """Fixture to provide the database URL."""
    DB_NAME = config("DB_NAME")
    return config("SQLALCHEMY_DATABASE_URL") + DB_NAME


def test_database_connection(database_url):
    """Test to check if the database connection is successful."""
    try:
        engine = create_engine(database_url, client_encoding='UTF8')
        with engine.connect() as connection:
            assert connection is not None, "Connection failed: connection is None"
            print("Connection successful")
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")
