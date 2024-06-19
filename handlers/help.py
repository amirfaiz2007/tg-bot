from aiogram.types import (Message)
from aiogram.filters import Command
from aiogram import Router
from markup import link_keyboard

router = Router()


@router.message(Command('help'))
async def help(message: Message):
    text = "/start - запустить бота▶️\n/help - показать доступные команды\n/about - информация\n/menu - главное меню бота"
    await message.answer(text=text)
    await message.delete()
