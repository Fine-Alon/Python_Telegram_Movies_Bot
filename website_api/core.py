import requests
from secret import token, f

print(token)
API_WEBSITE_KEY = f.decrypt(token.decode())


class RequestSiteApi:
    _URL = 'https://api.kinopoisk.dev/v1.4/movie'
    params = {
        'page': 1,
        'limit': 2,
    }

    def get_movie_by_name(self, outcome_params=None):
        """
        Выполняет запрос к API Кинопоиска для поиска фильмов по имени и возвращает
        выбранные параметры: название, описание, рейтинг, год, жанр, возрастной рейтинг, постер.

        :param outcome_params: Дополнительные параметры для поиска.
        :return: Список фильмов с нужными полями.
        """

        # Объединяем дефолтные параметры с новыми
        print('outcome_params: ', outcome_params)
        if outcome_params is None:
            outcome_params = {'query': 'Рокки'}

        final_params = self.params.copy()  # Создаем копию дефолтных параметров
        final_params.update({'query': outcome_params})  # Обновляем копию новыми параметрами
        r = requests.get(self._URL + '/search',
                         headers={'X-API-KEY': API_WEBSITE_KEY},
                         params=final_params)

        if r.status_code == 200:
            data = r.json().get('docs', [])  # Получаем список фильмов из ответа
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
        else:
            print('Response is not OK')
            return None

    def get_movie_by_rating(self, outcome_params=None):
        select_fields = ['name', 'description', 'releaseYears', 'rating', 'ageRating',
                         'genres', 'poster']  # Список полей требуемых в ответе из модели
        rating_kp = ['5-10']  # Поиск по рейтингу Кинопоиск (пример: 7, 10, 7.2-10)

        final_params = self.params.copy()
        final_params.update({'selectFields': select_fields, 'rating.kp': rating_kp})
        print('final_params ', final_params)
        if not outcome_params:
            r = requests.get(self._URL, headers={'X-API-KEY': API_WEBSITE_KEY}, params=final_params)
        else:
            rating_kp = [outcome_params]
            final_params.update({'rating.kp': rating_kp})
            r = requests.get(self._URL, headers={'X-API-KEY': API_WEBSITE_KEY}, params=final_params)

        if r.status_code == 200:
            print('r.json()  ', r.json())
            return r.json()
        else:
            return None


s = {'docs': [{'name': '....',
               'description': '....',
               'rating': {'kp': 8, 'imdb': 0, 'filmCritics': 0, 'russianFilmCritics': 0, 'await': None},
               'ageRating': 18, 'poster': {
        'url': 'https://.....',
        'previewUrl': 'https://....'},
               'genres': [{'name': 'документальный'}, {'name': 'криминал'}],
               'releaseYears': [{'start': 2016, 'end': None}]}, {'name': 'Основной инстинкт. Продолжение рода',
                                                                 'description': '....',
                                                                 'rating': {'kp': 8, 'imdb': 0, 'filmCritics': 0,
                                                                            'russianFilmCritics': 0, 'await': None},
                                                                 'ageRating': 6, 'poster': {
        'url': '....',
        'previewUrl': 'https:/....'},
                                                                 'genres': [{'name': 'документальный'}],
                                                                 'releaseYears': [{'start': 2021, 'end': 2021}]}],
     'total': 32, 'limit': 2, 'page': 1, 'pages': 16}
