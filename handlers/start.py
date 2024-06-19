from aiogram.filters import CommandStart
from aiogram.types import Message
from markup import form_button
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form
from erg import get_photo

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(Form.wait)
    text = "Привет! Перед началом необходимо заполнить небольшую анкету. Нажми на кнопку ниже, чтобы перейти к заполению"
    await message.answer(text=text, reply_markup=form_button)
    photo = await get_photo('animal')
    await message.answer_photo(photo=photo)






