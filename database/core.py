from peewee import SqliteDatabase, Model, CharField, DateField, IntegerField, BlobField

db = SqliteDatabase('movies.db')


class MoviesSearchHistory(Model):
    user_id = IntegerField()
    search_date = DateField()
    film_name = CharField(null=True)
    film_descr = CharField(null=True)
    film_rating = IntegerField(null=True)
    film_created_at = IntegerField(null=True)
    film_genre = CharField(null=True)
    age_rating = IntegerField(null=True)
    poster = BlobField(null=True)

    class Meta:
        database = db  # This model uses the 'movies.db' database.


db.connect()

db.create_tables([MoviesSearchHistory])
