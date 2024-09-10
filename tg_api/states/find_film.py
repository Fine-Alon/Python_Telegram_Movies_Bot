from telebot.states import State, StatesGroup


class FindFilmState(StatesGroup):
    name = State()
    rating = State()
    low_budget = State()
    high_budget = State()
