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

    def get_movie_by_name(self, params):
        """
       Выполняет запрос к API Кинопоиска для поиска фильмов по имени.

       :return: JSON-ответ от API с результатами поиска.
       """
        r = requests.get(self._URL + '/search',
                         headers={'X-API-KEY': API_WEBSITE_KEY},
                         params=params)

        if r.status_code == 200:
            print(r.json())
            return r.json()
        else:
            print('Response is not OK')
