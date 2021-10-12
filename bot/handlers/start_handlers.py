
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
    await message.answer(text='Привет! Ты попал в Телеграм бот.\n'
                              'Для получения общей информации о нашей деятельности нажми /help\n'
                              'Для отмены всех действий в любой момент нажмите /cancel')
    await AllStates.question_2.set()
    
        
    
# Question handler №2
@dp.message_handler(state=AllStates.question_2)
async def question_2_menu(message: types.Message):
    await message.answer(text='Вопрос 1', reply_markup=keybords.keyboard_2)
    
    await AllStates.question_3.set()
                    
    
# Question handler №3
@dp.message_handler(state=AllStates.question_3)
async def question_3_menu(message: types.Message):
    await message.answer(text='Вопрос 2', reply_markup=keybords.keyboard_3)
    
    await AllStates.question_4.set()
                    
    
# Question handler №4
@dp.message_handler(state=AllStates.question_4)
async def question_4_menu(message: types.Message):
    await message.answer(text='Вопрос 3', reply_markup=keybords.keyboard_4)
    
    await AllStates.question_5.set()
                    
    
# Question handler №5
@dp.message_handler(state=AllStates.question_5)
async def question_5_menu(message: types.Message):
    await message.answer(text='Вопрос 4', reply_markup=keybords.keyboard_5)
    
    await AllStates.question_6.set()
                    

# Question handler №6
@dp.message_handler(state=AllStates.question_6)
async def question_6_menu(message: types.Message):
    await message.answer(text='Вопрос 5', reply_markup=keybords.keyboard_6)
    
    await AllStates.question_7.set()
                    

# Question handler №7
@dp.message_handler(state=AllStates.question_7)
async def question_7_menu(message: types.Message):
    await message.answer(text='Вопрос 6', reply_markup=keybords.keyboard_7)
    
    await AllStates.question_8.set()
                    

# Question handler №8
@dp.message_handler(state=AllStates.question_8)
async def question_8_menu(message: types.Message):
    await message.answer(text='Вопрос 7', 
    reply_markup=types.ReplyKeyboardRemove())
