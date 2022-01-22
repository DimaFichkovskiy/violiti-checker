from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu_inl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Слідкувати за лотом", callback_data="Слідкувати за лотом"),
            InlineKeyboardButton(text="Перегляд моїх лотів", callback_data="Перегляд моїх лотів"),
        ],
        [
            InlineKeyboardButton(text="Допомога", callback_data="Допомога"),
        ]
    ]
)

# view_menu_inl = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Переглянути лоти які закінчуються протягом 10-ти годин", callback_data="Переглянути лоти що закінчуються"),
#         ],
#         [
#             InlineKeyboardButton(text="Вибрати конкретний лот для перегляду", callback_data="Вибрати конкретний лот"),
#         ]
#     ]
# )

#
# choice = InlineKeyboardMarkup(row_width=2)
#
# follow_the_lot = InlineKeyboardButton("Слідкувати за лотом", callback_data='/link')
# view_lots = InlineKeyboardButton("Перегляд лотів", callback_data="/view")
# help_bot = InlineKeyboardButton("Допомога", callback_data="/help")


