from peewee import *
#peewee is a lightweight library used as an ORM 


class Connection:
    # __function__ are python built-in functions
    def __init__(self):
        self.path: str = 'data.sqlite'

    def connect(self):
        sqlite_db = SqliteDatabase(self.path)
        return sqlite_db
