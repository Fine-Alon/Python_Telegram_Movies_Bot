from database.utils.CRUD import create_record


def select_data(res, user_id):
    data = res.json().get('docs', [])  # Получаем список фильмов из ответа
    movie_list = []
    # Проходимся по каждому фильму и извлекаем нужные поля
    for movie in data:
        movie_info = {
            'film_name': movie.get('name', 'N/A'),
            'film_descr': movie.get('description', 'N/A'),
            'film_rating': movie.get('rating', {}).get('kp', 'N/A'),
            'film_created_at': movie.get('year', 'N/A'),
            'film_genre': ', '.join([genre.get('name', 'N/A') for genre in movie.get('genres', [])]),
            'age_rating': movie.get('ageRating', 'N/A'),
            'poster': movie.get('poster', {}).get('url', 'N/A')
        }
        create_record(user_id, movie_info['film_name'], movie_info['film_descr'], movie_info['film_rating'],
                      movie_info['film_created_at'], movie_info['film_genre'],
                      movie_info['age_rating'], movie_info['poster'])

        movie_list.append(movie_info)
    return movie_list

