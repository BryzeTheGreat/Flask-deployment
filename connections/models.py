from connections.connect import Base, engine, Session
from sqlalchemy import Column, String, Integer

session = Session()

class Accounts(Base):
    __tablename__ = "users"
    
    uid = Column(String, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    
Base.metadata.create_all(bind=engine)
