# Dependencies Required for SqlAlchemy and PostGres #
```python
pip install psycopg2-binary
pip install SQLAlchemy
```

# Source code for CRUD operations #
```python
from sqlalchemy import create_engine


class PostGresDbUtil:

    @staticmethod
    def providepostgresbatabase():
        db_string = "postgresql://username:password@hostname:portnumber/databasename"
        db = create_engine(db_string)
        return db

```

```python
from postgresdbutil import PostGresDbUtil


def invokedb(db):
    # Create
    db.execute("CREATE TABLE IF NOT EXISTS employee (fullname text, companyname text, rank text)")
    db.execute("INSERT INTO employee (fullname, companyname, rank) VALUES ('Raj Bhatta', 'SST Wireless', 'Principal Developer')")

    # Read
    result_set = db.execute("SELECT * FROM employee")
    for r in result_set:
        print(r)

    # Update
    db.execute("UPDATE employee SET fullname='Niraj Bhatta' WHERE rank='Principal Developer'")

    # Delete
    db.execute("DELETE FROM employee WHERE rank='Principal Developer'")


if __name__ == "__main__":
    postgresDbUtil = PostGresDbUtil()
    invokedb(postgresDbUtil.providepostgresbatabase())

```