from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from classes import User, GREETING, HELP
from config import config as cfg
from db import Database
import datetime as dt
import os


class ClientState(StatesGroup):
    FREE = State()
    REGESTRATION_NAME = State()
    REGESTRATION_GRADE = State()


bot = Bot(token=cfg.bot_token)
dp = Dispatcher(bot)
db = Database(os.path.abspath(cfg.db_file))


async def send_text(chat: int, text: str):
    with open(text, 'r', encoding='utf-8') as f:
        await bot.send_message(chat, f.read())


@dp.message_handler(commands=["start"])
async def start(message: types.Message, state: FSMContext):
    chat = message.chat.id
    user = db.import_user(id=chat)
    if user is not None:
        pass
    else:
        await send_text(chat, GREETING)
        await state.set_state(ClientState.REGESTRATION_NAME)


@dp.message_handler(commands=["profile"])
async def profile(message: types.Message, state: FSMContext):
    chat = message.chat.id
    user = db.import_user(id=chat)
    if user is None:
        raise Exception
    else:
        pass


@dp.message_handler(commands=["order"])
async def order(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(commands=["help"])
async def help(message: types.Message, state: FSMContext):
    await send_text(chat, HELP)


@dp.message_handler(commands=["admin"])
async def admin(message: types.Message, state: FSMContext):
    pass


@dp.message_handler()
async def base(message: types.Message, state: FSMContext):
    await message.reply("Я вас не понимаю")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
