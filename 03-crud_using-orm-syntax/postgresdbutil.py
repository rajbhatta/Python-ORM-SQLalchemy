from sqlalchemy import create_engine


class PostGresDbUtil:

    @staticmethod
    def providepostgresbatabase():
        db_string = "postgresql://username:password@hostname:portnumber/databasename"
        db = create_engine(db_string)
        return db
