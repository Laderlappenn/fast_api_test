from fastapi import APIRouter, Body


from model.car import Car
import service.car as service

router = APIRouter(prefix="/car")


@router.get("")
def get_all() -> list[Car]:
    return service.get_all()


@router.get("/{car_id}", status_code=200, response_model=Car)
def get_one(car_id: int) -> Car:
    return service.get_one(car_id)


@router.post("", status_code=201)
def create(car: Car = Body()) -> Car:
    return service.create(car)


@router.patch("/{car_id}")
def modify(car_id: int, car: Car = Body()) -> Car:
    return service.modify(car_id, car)


@router.put("/{car_id}")
def replace(car_id: int, car: Car = Body()) -> Car:
    return service.replace(car_id, car)


@router.delete("/{car_id}")
def delete(car_id: int) -> bool:
    service.delete(car_id)
    return True



