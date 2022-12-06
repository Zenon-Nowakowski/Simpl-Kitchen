from typing import Text
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, Integer, Text
from database import Base


class Movie(Base):
    __tablename__ = "Movie"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    desc = Column(Text())
    type = Column(String(20))
    url = Column(String(100))
    rating = Column(Integer)


class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    instruction_id = Column(Integer, ForeignKey("instructions.id"))
    name = Column(String(50), unique=True)
    picture_url = Column(String(100))
    direction = Column(Text())


# class Instruction(Base):
#     __tablename__ = "instructions"
#     id = Column(Integer, primary_key=True, index=True)
#     narrative = Column(Text())


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(16), index=True)


class Recipe_Ingredient(Base):
    __tablename__ = "recipie_ingredients"
    recipie_id = Column(ForeignKey("recipes.id"), primary_key=True)
    ingredient_id = Column(ForeignKey("ingredients.id"), primary_key=True)
    quantity = Column(Integer)
