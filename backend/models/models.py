from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Province(Base):
    __tablename__ = 'province'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(Integer)




class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    email = Column(String)
    password = Column(String)