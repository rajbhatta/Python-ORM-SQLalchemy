from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Employee(base):
    __tablename__ = 'employee'
    fullname = Column(String, primary_key=True)
    companyname = Column(String)
    rank = Column(String)