from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from config import config as cfg
import datetime as dt
import os


class ClientState(StatesGroup):
    pass


storage = RedisStorage2()
bot = Bot(token=cfg.bot_token)
dp = Dispatcher(bot, storage=storage)
db = Database(os.path.abspath(cfg.db_file))
db.create_tables()


@dp.message_handler(commands=["start"])
async def start(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(commands=["profile"])
async def start(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(commands=["order"])
async def start(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(commands=["help"])
async def start(message: types.Message, state: FSMContext):
    pass


@dp.message_handler()
async def base(message: types.Message, state: FSMContext):
    pass


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
