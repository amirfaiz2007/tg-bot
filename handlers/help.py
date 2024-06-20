from aiogram.types import (Message)
from aiogram.filters import Command
from aiogram import Router
from markup import link_keyboard
from erg import get_photo

router = Router()


@router.message(Command('help'))
async def help(message: Message):
    photo = await get_photo('lake')
    await message.answer_photo(photo=photo)
    text = "/start - запустить бота▶️\n/help - показать доступные команды\n/about - информация\n/menu - главное меню бота"
    await message.answer(text=text)
    await message.delete()

