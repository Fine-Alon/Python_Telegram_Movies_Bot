import datetime
from database.core import MoviesSearchHistory


def create_record(user_id: int, film_name: str,
                  film_descr: str, film_rating: int, film_created_at: int,
                  film_genre: str, age_rating: int, poster):
    recorded_data = MoviesSearchHistory.create(
        user_id=user_id, search_data=datetime.datetime.now(), film_name=film_name,
        film_descr=film_descr, film_rating=film_rating, film_created_at=film_created_at,
        film_genre=film_genre, age_rating=age_rating, poster=poster
    )
    for movie in MoviesSearchHistory.select().where(MoviesSearchHistory.user_id == user_id).order_by(
            MoviesSearchHistory.search_data):
        print(
            'Film\'s name is {}, created at {}'.format(
                movie.film_name, movie.search_data))


def dell_record(user_id):
    deleted_records = MoviesSearchHistory.delete().where(MoviesSearchHistory.user_id == user_id).execute()
    return deleted_records


def get_record(user_id):
    try:
        record = MoviesSearchHistory.get(MoviesSearchHistory.user_id == user_id)
        return record
    except MoviesSearchHistory.DoesNotExist:
        return None
