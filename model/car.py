from pydantic import BaseModel


class Car(BaseModel):
    id: int
    name: str
    fuel: str
    price: str
    category: str
    link: str

