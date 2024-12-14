from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message
import logging
import button_bar as bb
import text
from decorators import  logger_function
router = Router()




@router.message(Command("start"))
@logger_function
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=bb.menu)
    # await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=bb.markup3)

 

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
@logger_function
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=bb.menu)


@router.message()
@logger_function
async def message_handler(msg: Message):
    with open('logg.txt', 'a', encoding='utf-8') as f: f.write(f'ПИШЕТ Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}\n')
    logging.info( f'ПИШЕТ Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}'  )
    await msg.answer(text.fuck)   


@router.callback_query(F.data == "generate_image")
@logger_function
async def start_handler_generate_image(msg: Message):
    with open('logg.txt', 'a', encoding='utf-8') as f: f.write(f'НАЖАЛ кнопку generate_image Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}\n')
    logging.info( f'НАЖАЛ кнопку generate_image Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}'  )
    await msg.answer(text.fuck, reply_markup=bb.menu)


@router.callback_query(F.data == "help")
@logger_function
async def start_handler_help(msg: Message):
    with open('logg.txt', 'a', encoding='utf-8') as f: f.write(f'НАЖАЛ кнопку help Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}\n')
    logging.info( f'НАЖАЛ кнопку help Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}'  )
    await msg.answer(text.fuck, reply_markup=bb.menu)



@router.callback_query(F.data == "generate_text")
@logger_function
async def start_handler_generate_text(msg: Message):
    with open('logg.txt', 'a', encoding='utf-8') as f: f.write(f'НАЖАЛ кнопку generate_text Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}\n')
    logging.info( f'НАЖАЛ кнопку generate_text Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}'  )
    await msg.answer(text.fuck, reply_markup=bb.menu)


@router.callback_query(F.data == "free_tokens")
@logger_function
async def start_handler_free_tokens(msg: Message):
    with open('logg.txt', 'a', encoding='utf-8') as f: f.write(f'НАЖАЛ кнопку free_tokens Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}\n')
    logging.info( f'НАЖАЛ кнопку free_tokens Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}'  )
    await msg.answer(text.fuck, reply_markup=bb.menu)


@router.callback_query(F.data == "balance")
@logger_function
async def start_handler_free_tokens(msg: Message):
    with open('logg.txt', 'a', encoding='utf-8') as f: f.write(f'НАЖАЛ кнопку balance Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}\n')
    logging.info( f'НАЖАЛ кнопку balance Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}'  )
    await msg.answer('нет у тебя ничего', reply_markup=bb.menu)


@router.callback_query(F.data == "website")
@logger_function
async def start_handler_free_tokens(msg: Message):
    with open('logg.txt', 'a', encoding='utf-8') as f: f.write(f'НАЖАЛ кнопку website Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}\n')
    logging.info( f'НАЖАЛ кнопку website Пользователь: {msg.from_user.full_name} с id {msg.from_user.id}'  )
    await msg.answer('нет у тебя ничего', reply_markup=bb.menu)