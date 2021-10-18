import os
import openpyxl


# Создаем клавиатуры
def creat_keyboards():
    try:
        file = open('bot/modules/keybords.py', 'w', encoding='utf-8')
    except:
        os.mkdir("bot")
        os.mkdir("modules")
        file = open('bot/modules/keybords.py', 'w', encoding='utf-8')
    start_text = """
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
"""
    excel = openpyxl.reader.excel.load_workbook(filename='creator.xlsx')
    excel.active = 0
    sheet = excel.active
    i = 2
    new_kb_text = ''
    btn_text = ''
    btn_add_text = ''
    proces = True
    while proces:
        if "reply" in str(sheet[f'D{i}'].value):
            new_kb_text = new_kb_text + f'''
keyboard_{i} = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)'''
            letters = ("E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O")
            for l in letters:
                if sheet[f'{l}{i}'].value is not None:
                    btn_text = btn_text + f"""                   
btn_{i}_{l} = KeyboardButton('{str(sheet[f'{l}{i}'].value)}')"""
                    btn_add_text = btn_add_text + f"""    
keyboard_{i}.add(btn_{i}_{l})"""
            i += 1
        elif "inline" in str(sheet[f'D{i}'].value):
            new_kb_text = new_kb_text + f'''
keyboard_{i} = InlineKeyboardMarkup()'''
            letters = ("E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O")
            for l in letters:
                if sheet[f'{l}{i}'].value is not None:
                    btn_text = btn_text + f"""                   
btn_{i}_{l} = InlineKeyboardButton(text='{str(sheet[f'{l}{i}'].value).split("###")[0]}', callback_data='{str(sheet[f'{l}{i}'].value).split("###")[1]}')"""
                    btn_add_text = btn_add_text + f"""    
keyboard_{i}.add(btn_{i}_{l})"""
            i += 1
        else:
            proces = False
    text = start_text + "\n" + new_kb_text + "\n" + btn_text +"\n" + btn_add_text
    file.write(text)
    file.close()
