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
    invokedb(PostGresDbUtil.providepostgresbatabase())
