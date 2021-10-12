
from aiogram.dispatcher.filters.state import State, StatesGroup


# Welcome form
class AllStates(StatesGroup):
        
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()
    question_6 = State()
    question_7 = State()
    question_8 = State()