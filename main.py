import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from googletrans import Translator

from config import TOKEN

import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = Translator()

@dp.message(F.photo)
async def react_photo(message: Message):
     list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
     rand_answ = random.choice(list)
     await message.answer(rand_answ)
     await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile("sampl.ogg")
    await message.answer_voice(voice)


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Приветики, {message.from_user.first_name}')

@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

@dp.message(F.text)
async def handle_text(message: Message):
    text_to_translate = message.text
    translated_text = translator.translate(text_to_translate, src='auto', dest='en').text
    await message.answer(translated_text)

@dp.message()
async def start(message: Message):
    await message.answer("Приветики, я бот!")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())