import os


# Создаем main.py
def creat_main():
    try:
        file = open('bot/main.py', 'w')
    except:
        os.mkdir("bot")
        file = open('bot/main.py', 'w')
    text = """
from aiogram import executor
from modules.dispatcher import dp
import __init__


if __name__ == '__main__':
    executor.start_polling(dp)
        """
    file.write(text)
    file.close()


# Создаем файл настроек телеграма
def creat_json():
    try:
        file = open('bot/telegram.json', 'w')
    except:
        os.mkdir("bot")
        file = open('bot/telegram.json', 'w')
    text = """
{
  "telegram_token": "1849931200:AAE1eurg0RIgrC2pU55WpLIi8diXiV-Jei8"
}
        """
    file.write(text)
    file.close()


# Создаем файл диспетчера
def creat_dispatcher():
    try:
        file = open('bot/modules/dispatcher.py', 'w')
    except:
        os.mkdir("bot/modules")
        file = open('bot/modules/dispatcher.py', 'w')
    text = """
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from modules.states import AllStates
import json


import logging

with open("telegram.json", 'r') as file:
    telegram_token = str(json.load(file)["telegram_token"])
    file.close()

storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(telegram_token)
dp = Dispatcher(bot, storage=storage)

        """
    file.write(text)
    file.close()


# Создаем __init__
def creat_init():
    try:
        file = open('bot/__init__.py', 'w')
    except:
        os.mkdir("bot")
        file = open('bot/__init__.py', 'w')
    text = """
from handlers import start_handlers

        """
    file.write(text)
    file.close()
