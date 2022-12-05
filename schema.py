from datetime import date
from pydantic import BaseModel


class Movie(BaseModel):
    id = int
    name = str
    desc = str
    type = str
    url = str
    rating = str
    data = date


class Recipie(BaseModel):
    id = int
    instruction_id = int
    name = str
    picture_url = str


class Instruction(BaseModel):
    id = int
    narrative = str


class Ingredient(BaseModel):
    id = int
    title = str

    class Config:
        orm_mode = True
