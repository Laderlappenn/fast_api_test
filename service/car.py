from model.car import Car
from data import car as data


def get_all() -> list[Car]:
    return data.get_all()


def get_one(car_id: int) -> Car:
    return data.get_one(car_id)


def create(car: Car) -> Car:
    return data.create(car)


def modify(car_id: int, car: Car) -> Car:
    return data.modify(car_id, car)


def replace(car_id: int, car: Car) -> Car:
    return data.replace(car_id, car)


def delete(car_id: int) -> bool:
    data.delete(car_id)
    return True