from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from decouple import config


def test_database_connection():
    db_name = config("DB_NAME")
    database_url = config("SQLALCHEMY_DATABASE_URL") + db_name
    try:
        engine = create_engine(database_url)
        with engine.connect() as connection:
            assert connection is not None, "Connection failed: connection is None"
            print("Connection successful: " + database_url)
    except OperationalError as e:
        raise e
