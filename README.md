# Python_Telegram_Movies_Bot

Here is Telegram Bot on Python that will help u get nice experience in finding movie to evening

This TG-bot or app will base on Monolith architecture that contain liers as:

1- API Telegram-Bot
2- API website
3- database

Database:
it uses tool ORM as peewee that help create DB by python code only

Code can be run by cloning the repository and
installing the required libraries with the following command:  pip install -r requirements.txt

The bot is launched using the command: python main.py

then you need get your own api key from @BotFather in TG api and put it to
.env in your 1st level of project as:
BOT_TOKEN = "Ваш токен для бота, полученный от @BotFather"
API_WEBSITE_KEY = "Ваш ключ полученный от API по адресу https://kinopoisk.dev/#api"

bot name is @FindBestMovieForYourEveningBot

commands:
● movie_search — search for a movie/TV series by title;
● movie_by_rating — search for movies/TV series by rating;
● low_budget_movie — search for movies/TV series with a low budget;

● high_budget_movie — search for movies/TV series with a high budget;
● history — ability to view the history of requests and search for a movie/TV series.
