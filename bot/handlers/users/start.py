import json

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.db.models import DBDriver

from loader import dp
import logging


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name
    user_dict = message.from_user.to_python()
    if DBDriver.user_existence_check(user_id):
        DBDriver.add_new_user(user_id, username, full_name)
        logging.info(f"Added new user:\n {json.dumps(user_dict, indent=4)}")

    await message.answer(f"Привіт, {full_name}")
