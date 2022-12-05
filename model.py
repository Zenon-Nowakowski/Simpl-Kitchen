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


class Recipes(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    instruction_id = Column(Integer, ForeignKey("instruction.id"))


class Instructions(Base):
    __tablename__ = "instructions"
    id = Column(Integer, primary_key=True, index=True)
    narrative = Column(String(50))
