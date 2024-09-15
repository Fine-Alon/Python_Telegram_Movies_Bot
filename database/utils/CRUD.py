import datetime
from database.core import MoviesSearchHistory


def create_record(user_id: int, film_name: str,
                  film_descr: str, film_rating: int, film_created_at: int,
                  film_genre: str, age_rating: int, poster):
    search_date = datetime.datetime.now()
    recorded_data = MoviesSearchHistory.create(
        user_id=user_id, search_date=search_date, film_name=film_name,
        film_descr=film_descr, film_rating=film_rating, film_created_at=film_created_at,
        film_genre=film_genre, age_rating=age_rating, poster=poster
    )
    for movie in MoviesSearchHistory.select().where(MoviesSearchHistory.user_id == user_id).order_by(
            MoviesSearchHistory.search_date):
        print(
            'Film\'s name is {}, created at {}'.format(
                movie.film_name, movie.search_date))


def dell_record(user_id):
    deleted_records = MoviesSearchHistory.delete().where(MoviesSearchHistory.user_id == user_id).execute()
    return deleted_records


def get_record(user_id, date=None):
    records_list = []
    try:
        if date == None:
            records = MoviesSearchHistory.select().where(MoviesSearchHistory.user_id == user_id).order_by(
                MoviesSearchHistory.search_date.desc())
        else:
            print('date: ', date)
            records = MoviesSearchHistory.select().where((MoviesSearchHistory.user_id == user_id)
                                                         & (MoviesSearchHistory.search_date == date)).order_by(
                MoviesSearchHistory.search_date.desc())
        for movie in records:
            records_list.append(
                f"Дата поиска: {movie.search_date}\n"
                f"Фильм: {movie.film_name}\n"
                f"Описание: {movie.film_descr}\n"
                f"Рейтинг: {movie.film_rating}\n"
                f"Год выпуска: {movie.film_created_at}\n"
                f"Жанры: {movie.film_genre}\n"
                f"Возрастной рейтинг: {movie.age_rating}\n"
                f"Постер: {movie.poster}\n"
                "------------------------------------"
            )
        return records_list
    except MoviesSearchHistory.DoesNotExist:
        return None
