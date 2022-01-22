from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    test = ("Список команд: ",
            "/start - Розбочати роботу з ботом",
            "/help - Отримати справку")

    await message.answer("\n".join(test))


