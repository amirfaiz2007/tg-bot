from aiogram.filters import CommandStart
from aiogram.types import Message
from markup import form_button
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form, Menu
from erg import get_photo
from database import check_profile

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    exists = await check_profile(message.from_user.id)
    if not exists:
        await state.set_state(Form.wait)
        text = "Привет! Перед началом необходимо заполнить небольшую анкету. Нажми на кнопку ниже, чтобы перейти к заполению!"
        await message.answer(text=text, reply_markup=form_button)
        photo = await get_photo('animal')
        await message.answer_photo(photo=photo)
    else:
        await message.answer("Авторизация успешна! Вы ранее регистрировались в нашем боте"
                             "(напишите в чат,если это были вы)")
        await state.set_state(Menu.menu)






