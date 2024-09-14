from peewee import SqliteDatabase, Model, CharField, DateField, IntegerField, BlobField

db = SqliteDatabase('movies.db')


class MoviesSearchHistory(Model):
    user_id = IntegerField()
    search_data = DateField()
    film_name = CharField()
    film_descr = CharField()
    film_rating = IntegerField()
    film_created_at = IntegerField()
    film_genre = CharField()
    age_rating = IntegerField()
    poster = BlobField()

    class Meta:
        database = db  # This model uses the 'movies.db' database.


db.connect()

db.create_tables([MoviesSearchHistory])
