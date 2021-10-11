
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                   
btn_2_D = KeyboardButton('Привет')                   
btn_3_D = KeyboardButton('Привет')                   
btn_3_E = KeyboardButton('спасибо')                   
btn_4_D = KeyboardButton('Привет')                   
btn_4_E = KeyboardButton('спасибо')                   
btn_4_F = KeyboardButton('кнопка 3')                   
btn_5_D = KeyboardButton('Привет')                   
btn_5_E = KeyboardButton('спасибо')                   
btn_5_F = KeyboardButton('кнопка 3')                   
btn_5_G = KeyboardButton('Кнопка 4')
    
keyboard_2.add(btn_2_D)    
keyboard_3.add(btn_3_D)    
keyboard_3.add(btn_3_E)    
keyboard_4.add(btn_4_D)    
keyboard_4.add(btn_4_E)    
keyboard_4.add(btn_4_F)    
keyboard_5.add(btn_5_D)    
keyboard_5.add(btn_5_E)    
keyboard_5.add(btn_5_F)    
keyboard_5.add(btn_5_G)