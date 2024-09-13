import requests
from secret import token, f

print(token)
API_WEBSITE_KEY = f.decrypt(token.decode())


class RequestSiteApi:
    _URL = 'https://api.kinopoisk.dev/v1.4/movie'
    params = {
        'page': 1,
        'limit': 10,
        'query': 'Рокки'
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
            outcome_params = {}
        final_params = self.params.copy()  # Создаем копию дефолтных параметров
        print('final_params 1 ', final_params)
        final_params.update({'query': outcome_params})  # Обновляем копию новыми параметрами
        print('final_params 2 ', final_params)
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

