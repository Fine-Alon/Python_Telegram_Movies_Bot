# Инициализация бота. Подключение всех необходимых модулей и запуск бота

from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config

storage = StateMemoryStorage()
bot = TeleBot(config.BOT_TOKEN, state_storage=storage, use_class_middlewares=True)
