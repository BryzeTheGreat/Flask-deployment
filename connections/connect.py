from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///test.db")

Base = declarative_base()

Session = sessionmaker(engine)

session = Session() 