from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from states import Form, Menu
from markup import menu_button, form_button
from markup import menu_points, oge, ege, ege_prof
from database import create_profile, edit_profile


router = Router()


@router.message(Form.wait)
async def waiting(message: Message, state: FSMContext):
    await state.update_data(id=message.from_user.id)
    if message.text.lower() == "перейти к анкете":
        await state.set_state(Form.name)
        text = "Введите имя"
        await message.answer(text=text)
    else:
        text = "Я тебя не понимаю( Нажми на кнопку ниже, чтобы начать заполнять анкету"
        await message.answer(text=text)

@router.message(Form.name)
async def name(message: Message, state: FSMContext):
    if message.text.isalpha():
        await state.update_data(name=message.text)
        await state.set_state(Form.age)
        name = message.text
        text = "Отлично! Введите возраст"
        await message.answer(text=text)
    else:
        text = "Введите корректное имя"
        await message.answer(text=text)

@router.message(Form.age)
async def name(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(Form.number)
        age = message.text
        text = "Отлично! Введите свой номер телефона "
        await message.answer(text=text)
    else:
        text = "Введите корректный возраст"
        await message.answer(text=text)

@router.message(Form.number)
async def name(message: Message, state: FSMContext):
    t = message.text
    if (t [:1] == "8" or t [:2] == "+7") and len(t) == 11:
        await state.update_data(phone=message.text)
        await state.set_state(Menu.menu)
        number = message.text
        text = "Отлично! Вы успешно прошли авторизацию"
        data_dict = await state.get_data()
        await create_profile(data_dict['id'])
        await edit_profile(data_dict['id'], data_dict['name'], data_dict['age'], data_dict['phone'])
        await message.answer(text=text, reply_markup=menu_button)

    else:
        text = "Введите корректный номер телефона"
        await message.answer(text=text)


















