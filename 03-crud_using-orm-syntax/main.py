from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from modal.employee import Employee
from postgresdbutil import PostGresDbUtil

"""
- We no longer need to import the Table class, but instead we import declarative_base and sessionmaker. 
- Instead of creating tables, we'll create Python classes that subclass declarative_base, and instead of making a connection to our database we'll ask for a session. 
- Both of these concepts are a higher layer of abstraction than the ones we used previously.
- As before we still create a database engine, and now we also instantiate a declarative_base. 
- Instead of defining our Employee class as a Table, we create a normal Python object which subclasses base and which defines __tablename__. 
- As before, we define the columns and column types for our Film object, but now we can use the attributes title, director, and year, instead of using the strings that we had before.
"""


def invokedb(db):
    Session = sessionmaker(db)
    session = Session()

    base = declarative_base()
    base.metadata.create_all(db)

    # Create
    employee = Employee(fullname="Niraj Bhatta", companyname="QHR Technologies", rank="CT0")
    session.add(employee)
    session.commit()

    # Read
    employees = session.query(Employee)
    for em in employees:
        print(em.fullname)

    # Update
    employee.fullname = "Biraj B"
    session.commit()

    # Delete
    session.delete(employee)
    session.commit()


if __name__ == "__main__":
    invokedb(PostGresDbUtil().providepostgresbatabase())
