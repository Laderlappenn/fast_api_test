# from pydantic import BaseModel


# class Car(BaseModel):
#     id: int
#     name: str
#     fuel: str
#     price: str
#     category: str
#     link: str

from sqlmodel import SQLModel, Field
class Car(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    fuel: str
    price: str
    category: str
    link: str