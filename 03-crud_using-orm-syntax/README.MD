# Dependencies Required for SqlAlchemy and PostGres #
```python
pip install psycopg2-binary
pip install SQLAlchemy
```

# CRUD operations using ORM #
- We no longer need to import the <b>Table</b> class, but instead we import <b>declarative_base</b> and <b>sessionmaker</b>.
- Instead of creating tables, we'll create Python classes that subclass <b>declarative_base</b>, and instead of making a connection to our database we'll ask for a session. Both of these concepts are a higher layer of abstraction than the ones we used previously.

- As before we still create a database engine, and now we also instantiate a <b>declarative_base</b>. Instead of defining our Employee class as a Table, we create a normal Python object which subclasses base and which defines __tablename__. 
- As before, we define the columns and column types for our Employee object, but now we can use the attributes fullname, companyname, and rank, instead of using the strings that we had before.

- <b>Sessions</b> have some complications and subtleties that we won't cover in detail here. 
- You can think of a session as an intelligent connection to our database that will watch what we're doing in our Python code and modify the database as necessary. 
- Sessions have one more layer of abstraction than you would expect — first we have to instantiate a <b>sessionmaker</b> and link it to our engine <b>(Session = sessionmaker(db))</b> and then we have to instantiate this to open an actual session <b>(session = Session())</b>. It's well worth reading all the nitty-gritty details of how sessions work in the official documentation.

- Our <b>declarative_base</b> also provides some shortcuts — For example, we create our table by calling <b>base.metadata.create_all()</b>, which examines the schema that we implicitly created by declaring the Employee class, and sends a <b>CREATE TABLE</b> command to our database.

- We can insert data into our database by instantiating Python objects and passing them to <b>session.add()</b>.
- In our earlier examples, we used a database connection which defaults to auto commit. Sessions do not have this default, so we need to call <b>session.commit()</b> after any changes to our database.
# Source code for CRUD operations #
```python
from sqlalchemy import create_engine

   1. PostGresDbUtil.py

class PostGresDbUtil:

    @staticmethod
    def providepostgresbatabase():
        db_string = "postgresql://username:password@hostname:portnumber/databasename"
        db = create_engine(db_string)
        return db

```

```python

    2.main.py

from postgresdbutil import PostGresDbUtil
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData

from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from modal.employee import Employee
from postgresdbutil import PostGresDbUtil

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
    postgresDbUtil = PostGresDbUtil()
    invokedb(postgresDbUtil.providepostgresbatabase())

```

### modal ###
```python
    
    modal.employee.py

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Employee(base):
    __tablename__ = 'employee'
    fullname = Column(String, primary_key=True)
    companyname = Column(String)
    rank = Column(String)
```