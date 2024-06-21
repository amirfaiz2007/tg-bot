from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    wait = State()
    name = State()
    age = State()
    number = State()

class Menu(StatesGroup):
    menu = State()
    point_1 = State()
    point_2 = State()
    point_3 = State()
    message = State()
