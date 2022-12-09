from datetime import date
from pydantic import BaseModel


class Recipe(BaseModel):
    id = int
    name = str
    picture_url = str
    direction = str


class Ingredient(BaseModel):
    id = int
    name = str


class Recipe_Ingredient(BaseModel):
    recipe_id = int
    ingredient_id: int
    quantity: int
    unit: str

    class Config:
        orm_mode = True
