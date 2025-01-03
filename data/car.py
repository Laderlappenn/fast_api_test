import json

from sqlalchemy.orm import Session

from model.db_init import engine
from model.car import Car
from error.exceptions import Missing, Duplicate


# TODO think where to put return type hints, in data or service crud funcs


def json_to_model(json_row: dict) -> Car:
    return Car(**json_row)


def row_to_model(row: tuple) -> Car:
    id, name, fuel, price, category, link = row
    return Car(id=id, name=name, fuel=fuel, price=price, category=category, link=link)


def model_to_dict(car: Car) -> dict:
    return car.dict()


def get_all() -> list[Car]:
    with Session(engine) as session:
        cars = session.query(Car).all()
        print(cars)
    return cars


def get_one(car_id: int) -> Car:
    with Session(engine) as session:
        car = session.query(Car).filter(Car.id == car_id).first()
    return car


def create(car: Car) -> Car:
    with Session(engine) as session:
        session.add(car)
        session.commit()
        session.refresh(car)  # Refresh the car object to get the updated state (e.g., generated ID) # WHY??
    return car


def modify(car_id: int, car: Car) -> Car:
    with Session(engine) as session:
        db_car = session.get(Car, car_id) # car.id
        if not db_car:
            raise Missing("Car not found")

        # Update only the fields provided (partial update)
        for key, value in car.__dict__.items():
            if key != "_sa_instance_state" and value is not None:
                setattr(db_car, key, value)

        session.commit()
        session.refresh(db_car)
    return car


def replace(car_id: int, car: Car) -> Car:
    """
       Replace an entire car record in the database.
       """
    with Session(engine) as session:
        db_car = session.get(Car, car_id) #car.id
        if not db_car:
            raise Missing("Car not found")

        # Replace all fields with the new car's data
        for key, value in car.__dict__.items():
            if key != "_sa_instance_state":
                setattr(db_car, key, value)

        session.commit()
        session.refresh(db_car)
    return car


def delete(car_id: int) -> bool:
    """
       Delete a car record from the database.
       """
    with Session(engine) as session:
        db_car = session.get(Car, car_id)
        if not db_car:
            raise Missing("Car not found")
        session.delete(db_car)
        session.commit()
    return True # what to return???