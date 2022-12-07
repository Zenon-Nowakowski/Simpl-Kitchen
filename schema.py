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


class Recipe(BaseModel):
    id = int
    name = str
    picture_url = str
    direction = str


# class Instruction(BaseModel):
#     id = int
#     narrative = str


class Ingredient(BaseModel):
    id = int
    title = str


class Recipe_Ingredient(BaseModel):
    recipe_id = int
    ingredient_id: int
    quantity: int
# Add unit column

    class Config:
        orm_mode = True
