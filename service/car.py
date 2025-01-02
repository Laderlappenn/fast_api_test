from model.car import Car
from data import car as data


def get_all() -> list[Car]:
    return data.get_all()


def get_one(name: str) -> Car:
    return data.get_one(name)


def create(car: Car) -> Car:
    return data.create(car)


def modify(car: Car) -> Car:
    return data.modify(car)


def replace(car: Car) -> Car:
    return data.replace(car)


def delete(car: Car) -> bool:
    data.delete(car)
    return True