import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from decouple import config


engine: Engine | None = None

def get_db(database_url: str|None = None, reset: bool = False):
     """Подключение к БД"""
     global engine
     if engine:
         if not reset:
            return
         engine = None
     if not database_url:
         db_name = config("DB_NAME")
         database_url = config("SQLALCHEMY_DATABASE_URL") + db_name # if is_test_mode: database_url = config("SQLALCHEMY_DATABASE_TEST_URL")
     engine = create_engine(database_url)

get_db()


# from sqlmodel import create_engine, Session, SQLModel
# from decouple import config
#
#
# from model.car import Car
#
# DB_NAME = config("DB_NAME")
# DATABASE_URL = config("SQLALCHEMY_DATABASE_URL") + DB_NAME
#
# engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL queries for debugging
# SQLModel.metadata.create_all(engine)
#
# # Create a new Car record
# new_car = Car(
#     #id=1,
#     name="Toyota Corolla",
#     fuel="Petrol",
#     price="20000",
#     category="Sedan",
#     link="https://example.com/toyota-corolla"
# )
#
# # Use a session to add the record to the database
# with Session(engine) as session:
#     session.add(new_car)
#     session.commit()
#
#
# with Session(engine) as session:
#     cars = session.query(Car).all()
#     for car in cars:
#         print(car)