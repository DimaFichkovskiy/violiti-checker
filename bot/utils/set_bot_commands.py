from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Отримати справку"),
            types.BotCommand("link", "Відправити силку для слідкування за лотом"),
            types.BotCommand("menu", "Відкрити меню"),
            types.BotCommand("lots", "Перегляд лотів"),
        ]
    )