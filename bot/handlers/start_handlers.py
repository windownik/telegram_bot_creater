
from aiogram import types
from main import dp
from aiogram.dispatcher.filters import Text
import logging
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from modules.states import AllStates
from modules import keybords

    
@dp.message_handler(state='*', commands=['start'])
async def question_2_menu(message: types.Message):
    await message.answer(text='Вопрос 1', reply_markup=keybords.keyboard_2)
    await AllStates.question_2.set()
    
    
@dp.message_handler(state=AllStates.question_2)
async def question_3_menu(message: types.Message):
    await message.answer(text='Вопрос 2', reply_markup=keybords.keyboard_3)
    await AllStates.question_3.set()
    
    
@dp.message_handler(state=AllStates.question_3)
async def question_4_menu(message: types.Message):
    await message.answer(text='Вопрос 3', reply_markup=keybords.keyboard_4)

                