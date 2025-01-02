import json


from model.car import Car


# TODO think where to put return type hints, in data or service crud funcs


def json_to_model(json_row: dict) -> Car:
    return Car(**json_row)


def row_to_model(row: tuple) -> Car:
    id, name, fuel, price, category, link = row
    return Car(id=id, name=name, fuel=fuel, price=price, category=category, link=link)


def model_to_dict(car: Car) -> dict:
    return car.dict()


def get_all() -> list[Car]:
    with open('fake_data/cars.json') as stream:
        cars = json.load(stream)
    return [json_to_model(car) for car in cars]


def get_one(name: str) -> Car:
    with open('fake_data/cars.json') as stream:
        car = json.load(stream)[0]
    return json_to_model(car)


def create(car: Car) -> Car:
    return car


def modify(car: Car) -> Car:
    return car


def replace(car: Car) -> Car:
    return car


def delete(car: Car) -> bool:
    return True