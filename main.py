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
    await bot.send_message(message.from_user.id, "Здравствуйте, чем могу вам помочь?", reply_markup=start_keyboard)


async def range_production_func(message: types.Message):
    await bot.send_message(message.from_user.id, "Ассортимент:", reply_markup=range_production_keyboard)


async def one_pod_func(message: types.Message):
    if message.text == 'Одноразки':
        await bot.send_message(message.from_user.id, 'Одноразки:', reply_markup=time_pod_keyboard)
    else:
        await bot.send_message(message.from_user.id, message.text)


# функции, который возвращают на шаг назад
async def back_to_start_func(message: types.Message):
    await bot.send_message(message.from_user.id, 'Чем могу вам помочь?', reply_markup=start_keyboard)


async def back_to_range_func(message: types.Message):
    await bot.send_message(message.from_user.id, "Ассортимент:", reply_markup=range_production_keyboard)

# -----------------------------ADMIN SIDE---------------------------------------

# -----------------------------OTHER SIDE--------------------------------------

# ----------------------------KEYBOARD SIDE-------------------------------------
# начальная клавиатура
trace_mail_btn, range_production_btn = KeyboardButton("Поставки в ближайшее время"), KeyboardButton("Ассортимент")
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.row(range_production_btn).row(trace_mail_btn)
# клавиаутура ассортимента
hqd_btn, pod_btn, back_to_start_btn = KeyboardButton('Одноразки'), KeyboardButton('Поды'), KeyboardButton('Назад')
range_production_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
range_production_keyboard.insert(hqd_btn).insert(pod_btn).row(back_to_start_btn)
# клавиутура одноразок
hqd_pod_btn, puff_pod_btn, back_to_range_btn = KeyboardButton("Hqd"), KeyboardButton("Puff"), KeyboardButton('Назад🛒')
time_pod_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
time_pod_keyboard.insert(hqd_pod_btn).insert(puff_pod_btn).row(back_to_range_btn)


# ----------------------------REGISTER FUNCS-------------------------------------
def client_func(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start')
    dp.register_message_handler(range_production_func, lambda message: message.text == 'Ассортимент')
    dp.register_message_handler(back_to_start_func, lambda message: message.text == 'Назад')
    dp.register_message_handler(back_to_range_func, lambda message: message.text == 'Назад🛒')
    dp.register_message_handler(one_pod_func, lambda message: message.text in ['Одноразки', 'Hqd', 'Puff'])


# ----------------------------CALL REG FUNCS-------------------------------------
client_func(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
