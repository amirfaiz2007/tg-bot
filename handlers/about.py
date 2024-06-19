from aiogram.types import (Message)
from aiogram.filters import Command
from aiogram import Router
from markup import link_keyboard

router = Router()



@router.message(Command('about'))
async def about(message:Message):
    text = "Информация о боте"
    await message.answer(text=text, reply_markup=link_keyboard)
    await message.delete()

