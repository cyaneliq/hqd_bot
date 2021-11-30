from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import os

bot = Bot(token=str(os.getenv('TOKEN')))
dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот вышел в онлайн")


# -----------------------------CLIENT SIDE---------------------------------------
async def bot_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Здравствуйте, чем могу вам помочь?")


# -----------------------------ADMIN SIDE---------------------------------------

# -----------------------------OTHER SIDE--------------------------------------

# ----------------------------KEYBOARD SIDE-------------------------------------
trace_mail,  = KeyboardButton("Поставки в ближайшее время")


# ----------------------------REGISTER FUNCS-------------------------------------
def client_func(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
