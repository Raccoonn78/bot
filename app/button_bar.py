from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, BotCommand
from aiogram.types import ReplyKeyboardRemove 
from aiogram.types.web_app_info import WebAppInfo
# InlineKeyboardButton(text="Open Webview", web_app=WebAppInfo(url="https://example.com/"))


menu = [
    [InlineKeyboardButton(text="🌤️ Погода", callback_data="weather"),
    InlineKeyboardButton(text="🥋 Тренировка", callback_data="balance")],
]


# Создаем асинхронную функцию
async def set_main_menu(bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')
    ]

    await bot.set_my_commands(main_menu_commands)

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

