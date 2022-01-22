from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_def = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Слідкувати за лотом"),
        ],
        [
            KeyboardButton(text="Як користуватись ботом?"),
        ],
    ]
)
