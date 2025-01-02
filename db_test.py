from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from decouple import config


# Database setup
DB_NAME = config("DB_NAME")
SQLALCHEMY_DATABASE_URL = config(f'SQLALCHEMY_DATABASE_URL') + f"{DB_NAME}"
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, client_encoding='UTF8')

# Attempt a simple connection to see if it works
try:
    with engine.connect() as connection:
        print("Connection successful")
except Exception as e:
    print(f"Error: {e}")