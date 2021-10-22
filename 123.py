import os
import openpyxl


# Создаем импорты
def create_start_text(start_handler_text: str = 'Привет! Ты попал в Телеграм бот'):
    text_standart = f"""
from aiogram import types
from main import dp
from aiogram.dispatcher.filters import Text
import logging
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from modules.states import AllStates
from modules import keybords


# Start menu
@dp.message_handler(commands=['start'], state='*')
async def start_menu(message: types.Message):
    await message.answer(text='{start_handler_text}')
    await AllStates.question_2.set()

        """
    return (text_standart)


# Создаем хэндлеры
def create_handler():
    try:
        file = open('bot/handlers/start_handlers.py', 'w', encoding='utf-8')
    except:
        os.mkdir("bot/handlers")
        file = open('bot/handlers/start_handlers.py', 'w', encoding='utf-8')
    excel = openpyxl.reader.excel.load_workbook(filename='creator.xlsx')
    excel.active = 0
    sheet = excel.active
    i = 2
    handlers_text = ''
    proces = True
    while proces:
        if sheet[f'B{i}'].value is not None:
            text = str(sheet[f'B{i}'].value)

            if 'data' not in str(sheet[f'A{i}'].value):
                state_text = str(sheet[f'A{i}'].value).split('###')[0]
                if "reply" in str(sheet[f'D{i}'].value):
                    handlers_text = handlers_text + f"""
# Question handler №{i}
@dp.message_handler(state=AllStates.question_{state_text})
async def question_{i}_menu(message: types.Message):
    await message.answer(text='{text}', reply_markup=keybords.keyboard_{i})"""
                elif "inline" in str(sheet[f'D{i}'].value):
                    handlers_text = handlers_text + f"""
# Question handler №{i}
@dp.message_handler(state=AllStates.question_{state_text})
async def question_{i}_menu(message: types.Message):
    await message.answer(text='{text}', reply_markup=keybords.keyboard_{i})"""
                else:
                    handlers_text = handlers_text + f"""
# Question handler №{i}
@dp.message_handler(state=AllStates.question_{state_text})
async def question_{i}_menu(message: types.Message):
    await message.answer(text='{text}', 
    reply_markup=types.ReplyKeyboardRemove())"""
                if sheet[f'B{i + 1}'].value is not None:
                    handlers_text = handlers_text + f"""
    await AllStates.question_{i + 1}.set()

                        """
                else:
                    pass
            else:
                pass
                haead_handler_text = ''
                if "reply" in str(sheet[f'D{i}'].value):
                    db_text = str(sheet[f'A{i}'].value).split('###')
                    for db in db_text:
                        if db is not None:
                            callback_text = db.split('№№№')[0]
                            stat_text = db.split('№№№')[1]
                            haead_handler_text = haead_handler_text + f"""
@dp.callback_query_handler(state={stat_text}, text='{callback_text}')"""
                    handlers_text = handlers_text + f"""
async def question_{i}_menu(call: types.CallbackQuery):
    await call.message.edit_text(text='{text}', reply_markup=keybords.keyboard_{i})"""

                elif "inline" in str(sheet[f'D{i}'].value):
                    db_text = str(sheet[f'A{i}'].value).split('###')
                    for db in db_text:
                        if len(db) > 1:
                            callback_text = db.split('№№№')[0]
                            stat_text = db.split('№№№')[1]
                            haead_handler_text = haead_handler_text + f"""
@dp.callback_query_handler(state={stat_text}, text='{callback_text}')"""
                    handlers_text = handlers_text + haead_handler_text + f"""
async def question_{i}_menu(call: types.CallbackQuery):
    await call.message.edit_text(text='{text}', reply_markup=keybords.keyboard_{i})"""
                if sheet[f'B{i + 1}'].value is not None:
                    handlers_text = handlers_text + f"""
    await AllStates.question_{i + 1}.set()

"""
                else:
                    pass
            i += 1
        else:
            proces = False

    file.write(create_start_text() + handlers_text)
    file.close()
