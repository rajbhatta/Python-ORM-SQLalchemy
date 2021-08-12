# Dependencies Required for SqlAlchemy and PostGres #
```python
pip install psycopg2-binary
pip install SQLAlchemy
```

# CRUD operations using SQL expression language #
- Here I'm doing exactly same operation I have done in step 1 but using the SQL Expression Language that SQLAlchemy provides, instead of using raw SQL strings. 
- We'll see that this code is a little bit more verbose, and also fairly complicated and difficult to read, so we don't gain that much over the raw SQL queries above

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

def invokedb(db):
    meta = MetaData(db)
    employee_table = Table('employee', meta,
                       Column('fullname', String),
                       Column('companyname', String),
                       Column('rank', String))

    with db.connect() as conn:
        # Create
        employee_table.create()
        insert_statement = employee_table.insert().values(fullname="Raj Bhatta", companyname="SST Wireless", rank="Principal Developer")
        conn.execute(insert_statement)

        # Read
        select_statement = employee_table.select()
        result_set = conn.execute(select_statement)
        for r in result_set:
            print(r)

        # Update
        update_statement = employee_table.update().where(employee_table.c.rank == "Principal Developer").values(fullname="Raj Bhatta")
        conn.execute(update_statement)

        # Delete
        delete_statement = employee_table.delete().where(employee_table.c.rank == "CTO")
        conn.execute(delete_statement)


if __name__ == "__main__":
    postgresDbUtil = PostGresDbUtil()
    invokedb(postgresDbUtil.providepostgresbatabase())
```