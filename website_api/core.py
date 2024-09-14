import requests
from secret import token, f
from website_api.utils.select_responce_data import select_data

API_WEBSITE_KEY = f.decrypt(token.decode()).decode()


class RequestSiteApi:
    _URL = 'https://api.kinopoisk.dev/v1.4/movie'
    params = {
        'page': 1,
        'limit': 2,
        'timeout': 10
    }
    headers = {
        "accept": "application/json",
        "X-API-KEY": API_WEBSITE_KEY
    }

    def get_movie_by_name(self, user_id, outcome_params=None):
        """
        Выполняет запрос к API Кинопоиска для поиска фильмов по имени и возвращает
        выбранные параметры: название, описание, рейтинг, год, жанр, возрастной рейтинг, постер.

        :param outcome_params: Дополнительные параметры для поиска.
        :return: Список фильмов с нужными полями.
        """
        print('name')
        # Объединяем дефолтные параметры с новыми
        if outcome_params is None:
            outcome_params = {'query': 'Рокки'}

        final_params = self.params.copy()  # Создаем копию дефолтных параметров
        final_params.update({'query': outcome_params})  # Обновляем копию новыми параметрами
        r = requests.get(self._URL + '/search',
                         headers={'X-API-KEY': API_WEBSITE_KEY},
                         params=final_params)

        if r.status_code == 200:
            movie_list = select_data(r, user_id)
            return movie_list
        else:
            print('Response is not OK')
            return None

    def get_movie_by_rating(self, user_id, outcome_params=None):
        print('rating')
        select_fields = ['name', 'description', 'year', 'rating', 'ageRating',
                         'genres', 'poster']  # Список полей требуемых в ответе из модели
        rating_kp = ['5-10']  # Поиск по рейтингу Кинопоиск (пример: 7, 10, 7.2-10)

        final_params = self.params.copy()
        final_params.update({'selectFields': select_fields, 'rating.kp': rating_kp})

        if not outcome_params:
            r = requests.get(self._URL, headers=self.headers, params=final_params)
        else:
            rating_kp = [outcome_params]
            final_params.update({'rating.kp': rating_kp})
            r = requests.get(self._URL, headers=self.headers, params=final_params)

        if r.status_code == 200:
            movie_list = select_data(r, user_id)
            return movie_list
        else:
            print('Response is not OK')
            return None

    def get_movie_by_low_budget(self, user_id, outcome_params=None):
        print('low_budget')
        final_params = self.params.copy()
        budget_value = ['10000-100000000']
        final_params.update({'budget.value': budget_value, 'limit': outcome_params})
        r = requests.get(self._URL, headers=self.headers, params=final_params)

        if r.status_code == 200:
            movie_list = select_data(r, user_id)
            return movie_list
        else:
            print('Response is not OK')
            return None

    def get_movie_by_high_budget(self, user_id, outcome_params=None):
        final_params = self.params.copy()
        budget_value = ['100000001-1000000000']
        final_params.update({'budget.value': budget_value, 'limit': outcome_params})
        r = requests.get(self._URL, headers=self.headers, params=final_params)

        if r.status_code == 200:
            movie_list = select_data(r, user_id)
            return movie_list
        else:
            print('Response is not OK')
            return None
