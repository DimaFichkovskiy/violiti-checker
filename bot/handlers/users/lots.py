import emoji
from loader import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from keyboards.inline import menu_inl


@dp.message_handler(Command("lots"))
async def show_menu(message: Message):
    await message.answer(f"{emoji.emojize('🔎')} Оберіть спосіб перегляду лотів",
                         reply_markup=menu_inl.view_menu_inl)
