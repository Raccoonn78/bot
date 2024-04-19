from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст-хуекс", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
    [InlineKeyboardButton(text="💳 Купить токены-хуекены", callback_data="buy_tokens"),
    InlineKeyboardButton(text="💰 Баланс-хуянс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Партнёрская программа хуй там", callback_data="ref"),
    InlineKeyboardButton(text="🎁 Бесплатные токены-хуекены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь (себе помоги)", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

