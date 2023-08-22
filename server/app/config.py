import sqlalchemy
from databases import Database


DATABASE_URL = "sqlite:///home_automation.db"
database = Database(DATABASE_URL)
test_database = Database(DATABASE_URL, force_rollback=True)
sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)


def get_database() -> Database:
    return database


def get_test_db_url() -> Database:
    return test_database