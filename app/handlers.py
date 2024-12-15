from aiogram import F, Router, types
import aiogram.utils.markdown as fmt
import datetime
from aiogram.filters import Command
from aiogram.types import Message
import logging
import button_bar as bb
import text
from decorators import  logger_function
import requests

from aiogram import Bot, Dispatcher
import config
# from main import bot
router = Router()


bot = Bot(token=config.API_TOKEN )

@router.message(Command("start"))
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


@router.callback_query(F.data == "weather")
@logger_function
async def start_handler_weather(msg: Message):
    conditions= None
    temp= None
    temp_min= None
    temp_max= None
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'id': config.CITY_ID, 'units': 'metric', 'lang': 'ru', 'APPID': config.APPID})
        data = res.json()
        print(data)
        conditions=data['weather'][0]['description']
        temp= data['main']['temp']
        temp_min= data['main']['temp_min']
        temp_max= data['main']['temp_max']
    except Exception as e:
        print("Exception (weather):", e)
        pass
    await bot.send_message( chat_id=msg.from_user.id,  
                           text=f'''
Погода на сегодня 🤟: {datetime.datetime.today().year}-{datetime.datetime.today().month}-{datetime.datetime.today().day}
Москва: {conditions}
Температура сейчас: {temp}°C
Минимальная температура на сегодня: {temp_min}°C
Максимальная температура на сегодня: {temp_max}°C
А если выйдешь на улицу то будет невероятно солнечно 💙
                            ''',
                        #    text=fmt.text(
                        #         fmt.text(fmt.hunderline("Погода на сегодня"), ": ", fmt.hbold(str(datetime.datetime.today()))),
                        #         fmt.text(fmt.hstrikethrough(conditions)),
                        #         fmt.text("Температура сейчас:", fmt.hbold(temp), "°C"),
                        #         fmt.text("Минимальная температура на сегодня:", fmt.hbold(temp_min), "°C"),
                        #         fmt.text("Максимальная температура на сегодня:", fmt.hbold(temp_max), "°C"),
                        #         fmt.text("А если выйдешь на улицу то будет невероятно солнечно"),
                        #         sep="\n"
                        # )
                        parse_mode="HTML", reply_markup=bb.menu)# parse_mode="HTML", reply_markup=bb.menu




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