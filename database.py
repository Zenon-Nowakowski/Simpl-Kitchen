from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector as mysql

HOST = "104.237.135.4"
DATABASE = "simplkitchen"
USER = "remote"
PASSWORD = "1234"

db_connection = mysql.connect(
    host=HOST, database=DATABASE, user=USER, password=PASSWORD)

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:VLyFUBhvfiVcXn3@localhost:3306/serversiderendering"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
