def select_data(res):
    data = res.json().get('docs', [])  # Получаем список фильмов из ответа
    movie_list = []
    # Проходимся по каждому фильму и извлекаем нужные поля
    for movie in data:
        movie_info = {
            'Название': movie.get('name', 'N/A'),
            'Описание': movie.get('description', 'N/A'),
            'Рейтинг': movie.get('rating', {}).get('kp', 'N/A'),
            'Год производства': movie.get('year', 'N/A'),
            'Жанр': ', '.join([genre.get('name', 'N/A') for genre in movie.get('genres', [])]),
            'Возрастной рейтинг': movie.get('ageRating', 'N/A'),
            'Постер': movie.get('poster', {}).get('url', 'N/A')
        }
        movie_list.append(movie_info)
    return movie_list
