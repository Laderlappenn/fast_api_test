from fastapi import APIRouter


from model.car import Car
import service.car as service

router = APIRouter(prefix="/car")


@router.get("/")
def get_all() -> list[Car]:
    return service.get_all()


@router.get("/{name}", status_code=200)
def get_one(name: str) -> Car:
    return service.get_one(name)


@router.post("")
@router.post("/", status_code=201)
def create(car: Car) -> Car:
    return service.create(car)


@router.patch("")
@router.patch("/")
def modify(car: Car) -> Car:
    return service.modify(car)


@router.put("")
@router.put("/")
def replace(car: Car) -> Car:
    return service.replace(car)


@router.delete("")
@router.delete("/")
def delete(car: Car) -> bool:
    return service.delete(car)



