from peewee import *

db = SqliteDatabase('movies.db')


class Movies(Model):
    name = CharField()

    class Meta:
        database = db
