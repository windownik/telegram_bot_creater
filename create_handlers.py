import os
import openpyxl


# Создаем импорты
def create_import_start_text():
    text_standart = f"""
from aiogram import types
from main import dp
from aiogram.dispatcher.filters import Text
import logging
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from modules.states import AllStates
from modules import keybords

    """
    return(text_standart)


# Создаем начальный state c командным словом
def previous_state_with_command(text: str):
    command_text = str(text.split('__')[1])
    state_text = str(text.split('__')[2])
    if '*' in state_text:
        ret_text = f"""
@dp.message_handler(state='{state_text}', commands=['{command_text}'])"""
    else:
        ret_text = f"""
@dp.message_handler(state=AllStates.question_{state_text}, commands=['{command_text}'])"""
    return ret_text


# Создаем state c MessageHandler
def message_state(text: str):
    state_text = str(text.split('__')[1])
    if '*' in state_text:
        ret_text = f"""
@dp.message_handler(state='{state_text}')"""
    else:
        ret_text = f"""
@dp.message_handler(state=AllStates.question_{state_text})"""
    return ret_text


# Создаем state c CallbackHandler
def call_back_state(text: str):
    state_text = str(text.split('__')[1])
    callback_text = str(text.split('__')[2])
    ret_text = f"""
@dp.callback_query_handler(state={state_text}, text='{callback_text}')"""
    return ret_text


# Создаем основной текст хэндлера c CallbackHandler c клавиатурой
def callback_main_text_kb(text: str, index: int):
    ret_text = f"""
async def question_{str(index)}_menu(call: types.CallbackQuery):
    await call.message.edit_text(text='{text}', reply_markup=keybords.keyboard_{str(index)})"""
    return ret_text


# Создаем основной текст хэндлера простой либо с command c клавиатурой
def message_handler_main_text_kb(text: str, index: int):
    ret_text = f"""
async def question_{str(index)}_menu(message: types.Message):
    await message.answer(text='{text}', reply_markup=keybords.keyboard_{str(index)})"""
    return ret_text


# Создаем основной текст хэндлера c CallbackHandler без клавиатуры
def callback_main_text(text: str, index: int):
    ret_text = f"""
async def question_{str(index)}_menu(call: types.CallbackQuery):
    await call.message.edit_text(text='{text}')"""
    return ret_text


# Создаем основной текст хэндлера простой либо с command без клавиатуры
def message_handler_main_text(text: str, index: int):
    ret_text = f"""
async def question_{str(index)}_menu(message: types.Message):
    await message.answer(text='{text}')"""
    return ret_text


# Создаем хэндлеры
def create_handler():
    excel = openpyxl.reader.excel.load_workbook(filename='creator.xlsx')
    excel.active = 0
    sheet = excel.active
    i = 2
    handlers_text = ''
    proces = True
    while proces:
        if sheet[f'B{i}'].value is not None:                  # Открываем все ячейки с основным текстом по порядку
            data = str(sheet[f'A{i}'].value).split('###')     # Открываем стэйты
            state_text = ''
            for k in data:
                if 'Command__' in str(k):                     # Проверяем на наличие команды
                    state_text = state_text + previous_state_with_command(str(k))
                elif 'Message__' in str(k):                   # Проверяем на наличие message
                    state_text = state_text + message_state(str(k))
                elif 'CallBack__' in str(k):                       # Проверяем на наличие CallBack
                    state_text = state_text + call_back_state(str(k))

            main_data = str(sheet[f'B{i}'].value).split('###')     # Открываем текст хэндлера
            handler_text = ''
            for k in main_data:
                if sheet[f'B{i}'].value is not None:
                    if 'CallBack__' in str(data):                                # Проверяем на наличие CallBack с клавиатурой
                        handler_text = callback_main_text_kb(str(k), index=i)
                    else:                                                        # Создаем простой хэндлер с клавиатурой
                        handler_text = message_handler_main_text_kb(str(k), index=i)
                else:
                    if 'CallBack__' in str(data):                                # Проверяем на наличие CallBack с клавиатурой
                        handler_text = callback_main_text(str(k), index=i)
                    else:                                                        # Создаем простой хэндлер с клавиатурой
                        handler_text = message_handler_main_text(str(k), index=i)

            if sheet[f'C{i}'].value is not None:                                 # Устанавливаем следующий стэйт
                next_state_index = str(sheet[f'C{i}'].value).split('###')[0]
                next_state_text = f"""
    await AllStates.question_{next_state_index}.set()
    
    """
            else:
                next_state_text = f"""

                """

            handlers_text = handlers_text + state_text + handler_text + next_state_text
            i += 1
        else:
            proces = False

    handlers_text = create_import_start_text() + handlers_text

    try:
        file = open('bot/handlers/start_handlers.py', 'w', encoding='utf-8')
    except:
        os.mkdir("bot/handlers")
        file = open('bot/handlers/start_handlers.py', 'w', encoding='utf-8')

    file.write(handlers_text)
    file.close()

