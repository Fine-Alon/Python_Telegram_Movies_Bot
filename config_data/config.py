import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_WEBSITE_KEY = os.getenv("API_WEBSITE_KEY")
DEFAULT_COMMANDS = (
    ("help", "Вывести справку"),
    ("start", "Запустить бота"),
    ("menu", "Главное меню"),
    ("history", "Вывести историю запросов"),
    ("search", "Искать фильм"),
)
