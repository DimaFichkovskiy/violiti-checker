import asyncio
from datetime import datetime

from loader import dp
from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove, InputMediaPhoto
from keyboards.inline import menu_inl
from aiogram.dispatcher.filters import Command, Text, CommandHelp
import emoji

from utils.db.models import DBDriver
from loader import bot
from parser.violity.violity_parser import get_data_on_lot


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer(f"{emoji.emojize('📜')} Меню бота",
                         reply_markup=menu_inl.main_menu_inl)


@dp.callback_query_handler(text="Слідкувати за лотом")
async def add_lot(callback_query: types.CallbackQuery):
    await callback_query.answer(cache_time=60)
    await bot.send_message(callback_query.from_user.id,
                           "Ок, для цього відправте силку на лот!")


@dp.message_handler(text_contains="https://violity.com/")
async def get_link(message: Message):
    data_about_lot = get_data_on_lot(message.text)
    if DBDriver.lot_existence_check(message.text):
        date_string = data_about_lot['finish_date'] + ", " + data_about_lot['finish_time']
        date_formatter = "%d.%m.%Y, %H:%M:%S"
        date_and_time = datetime.strptime(date_string, date_formatter)

        DBDriver.add_new_lot(message.from_user.id, message.text, date_and_time)

        media = [InputMediaPhoto(
            media=data_about_lot['photos_url'][0],
            caption=(f"Ви тепер відслідковуєте: <b>{data_about_lot['name']}</b> \n\n"
                     f"⌛ <u>Час закінчення:</u> {data_about_lot['finish_date']}, {data_about_lot['finish_time']} \n"
                     f"💰 <u>Поточна ціна:</u> {data_about_lot['current_price_UAH']} грн ≈ {data_about_lot['current_price_USD']} $ \n\n"
                     f"<a href='{message.text}'>{emoji.emojize(':eyes:')} Переглянути лот в браузері</a>"))]

        for i in range(1, len(data_about_lot['photos_url'])):
            media.append(InputMediaPhoto(data_about_lot['photos_url'][i]))
        await message.answer_media_group(media)

    else:
        media = [InputMediaPhoto(
            media=data_about_lot['photos_url'][0],
            caption=(f"{emoji.emojize('🤔')} Хмм... \nЗдається ви вже відслідковуєте: <b>{data_about_lot['name']}</b> \n\n"
                     f"⌛ <u>Час закінчення:</u> {data_about_lot['finish_date']}, {data_about_lot['finish_time']} \n"
                     f"💰 <u>Поточна ціна:</u> {data_about_lot['current_price_UAH']} грн ≈ {data_about_lot['current_price_USD']} $ \n\n"
                     f"<a href='{message.text}'>{emoji.emojize(':eyes:')} Переглянути лот в браузері</a>"))]

        for i in range(1, len(data_about_lot['photos_url'])):
            media.append(InputMediaPhoto(data_about_lot['photos_url'][i]))
        await message.answer_media_group(media)

    # await asyncio.sleep(1)
    # await message.delete()


@dp.callback_query_handler(text="Перегляд моїх лотів")
async def view_lots(callback_query: types.CallbackQuery):
    # await callback_query.answer(cache_time=60)
    await callback_query.answer(text=f"{emoji.emojize('📩')} Завантаження...")
    # await asyncio.sleep(3)
    data = DBDriver.get_all_lots(callback_query.from_user.id)
    for d in data:
        lot_url = d['link']
        data_about_lot = get_data_on_lot(lot_url)
        media = [InputMediaPhoto(
            media=data_about_lot['photos_url'][0],
            caption=(f"Назва лота: <b>{data_about_lot['name']}</b> \n\n"
                     f"⌛ <u>Час закінчення:</u> {data_about_lot['finish_date']}, {data_about_lot['finish_time']} \n"
                     f"💰 <u>Поточна ціна:</u> {data_about_lot['current_price_UAH']} грн ≈ {data_about_lot['current_price_USD']} $ \n\n"
                     f"<a href='{lot_url}'>{emoji.emojize(':eyes:')} Переглянути лот в браузері</a>"))]

        for i in range(1, len(data_about_lot['photos_url'])):
            media.append(InputMediaPhoto(data_about_lot['photos_url'][i]))
        await callback_query.message.answer_media_group(media)

# @dp.callback_query_handler(text="Перегляд моїх лотів")
# async def show_view_lots_menu(callback_query: types.CallbackQuery):
#     await callback_query.message.edit_reply_markup(reply_markup=menu_inl.view_menu_inl)
# @dp.callback_query_handler(text="Переглянути лоти що закінчуються")
# async def view_ending_lots(callback_query: types.CallbackQuery):
#     data = DBDriver.get_lots_end(callback_query.from_user.id)
#     print(data)
