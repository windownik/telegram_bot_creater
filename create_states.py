import os
import openpyxl


# Создаем state
def creat_states():
    try:
        file = open('bot/modules/states.py', 'w')
    except:
        os.mkdir("bot/modules")
        file = open('bot/modules/states.py', 'w')
    excel = openpyxl.reader.excel.load_workbook(filename='creator.xlsx')
    excel.active = 0
    sheet = excel.active
    i = 2
    questions_text = ''
    proces = True
    while proces:
        if sheet[f'B{i}'].value is not None:
            questions_text = questions_text + f"""
    question_{i} = State()"""
            i += 1
        else:
            proces = False

    text = """
from aiogram.dispatcher.filters.state import State, StatesGroup


# Welcome form
class AllStates(StatesGroup):
        """
    file.write(text + questions_text)
    file.close()
