from telebot.handler_backends import State, StatesGroup


class FindFilmState(StatesGroup):
    film = State()
    genre = State()
