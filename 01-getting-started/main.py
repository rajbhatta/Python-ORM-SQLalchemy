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
