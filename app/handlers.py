from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import button_bar
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=button_bar.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=button_bar.menu)

@router.message()
async def message_handler(msg: Message):
    await msg.answer(text.fuck)

@router.callback_query(F.data == "generate_image")
async def start_handler_generate_image(msg: Message):
    await msg.answer(text.fuck, reply_markup=button_bar.menu)

@router.callback_query(F.data == "help")
async def start_handler_help(msg: Message):
    await msg.answer(text.fuck, reply_markup=button_bar.menu)


@router.callback_query(F.data == "generate_text")
async def start_handler_generate_text(msg: Message):
    await msg.answer(text.fuck, reply_markup=button_bar.menu)

@router.callback_query(F.data == "free_tokens")
async def start_handler_free_tokens(msg: Message):
    await msg.answer(text.fuck, reply_markup=button_bar.menu)


@router.callback_query(F.data == "balance")
async def start_handler_free_tokens(msg: Message):
    await msg.answer('нет у тебя ничего', reply_markup=button_bar.menu)