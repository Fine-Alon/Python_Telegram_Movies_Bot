def select_data(res):
    data = res.json().get('docs', [])  # Получаем список фильмов из ответа
    movie_list = []
    # Проходимся по каждому фильму и извлекаем нужные поля
    for movie in data:
        print(movie)
        movie_info = {
            'film_name': movie.get('name', 'N/A'),
            'film_descr': movie.get('description', 'N/A'),
            'film_rating': movie.get('rating', {}).get('kp', 'N/A'),
            'film_created_at': movie.get('year', 'N/A'),
            'film_genre': ', '.join([genre.get('name', 'N/A') for genre in movie.get('genres', [])]),
            'age_rating': movie.get('ageRating', 'N/A'),
            'poster': movie.get('poster', {}).get('url', 'N/A')
        }

        movie_list.append(movie_info)
    return movie_list


