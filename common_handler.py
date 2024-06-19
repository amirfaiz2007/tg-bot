from aiogram.filters import Command
from aiogram.types import Message, InputMediaPhoto
from markup import menu_points, oge, ege, ege_prof, help_points, link_keyboard
from aiogram import Router
from aiogram.fsm.context import FSMContext
from markup import menu_button, form_button
from states import Form, Menu



router = Router()
data = []


@router.message(Menu.menu)
async def menu(message: Message, state: FSMContext):
    await state.set_state(Menu.point_1)
    await message.answer (text="<b>Меню:</b>\n\nЗадания ОГЭ по математике.📝"
            "\n\nЗадания ЕГЭ по математике.👨🏻‍🎓"
            "\n\nЗадания ЕГЭ по профильной математике.🤓", reply_markup=menu_points, parse_mode="html")


@router.message(Menu.point_1)
async def menu_actions(message: Message, state: FSMContext):
    if message.text.lower() == "задания огэ по математике.📝":
        await message.answer(text="<b>Задания ОГЭ по математике.</b>\n Нажмите ниже чтобы перейти на сайт", reply_markup= oge, parse_mode="html")
    elif message.text.lower() == "задания егэ по математике.👨🏻‍🎓":
        await message.answer(text="<b>Задания ЕГЭ по математике.</b>\nНажмите ниже чтобы перейти на сайт", reply_markup= ege, parse_mode="html")
    elif message.text.lower() == "задания егэ по профильной математике.🤓":
        await message.answer(text="<b>Задания ЕГЭ по профильной математике.</b>\nНажмите ниже чтобы перейти на сайт", reply_markup= ege_prof, parse_mode="html")
    elif message.text == "/about":
        text = "Информация о боте"
        await message.answer(text=text, reply_markup=link_keyboard)
        await message.delete()
    elif message.text == "/start":
        await state.set_state(Form.wait)
    elif message.text == "/menu":
        await message.answer("Извините вы и так находитесь в меню")
    else:
        await state.set_state(Menu.point_2)
        text = 'Нет такого врианта ответа, если хотите увидеть весь список команд бота повторите свой запрос'
        await message.answer(text=text)

@router.message(Menu.point_2)
async def help(message: Message, state: FSMContext):
    await state.set_state(Menu.point_3)
    text = "запустить бота▶️\nпоказать доступные команды🆘\nинформация о боте❗\nглавное меню бота♾️"
    await message.answer(text=text, reply_markup=help_points, parse_mode="html")
    await message.delete()



@router.message(Menu.point_3)
async def help_actions(message: Message, state: FSMContext):
    if message.text.lower() == "запустить бота заново▶️" or message.text == "/start":
        await state.set_state(Form.wait)
        text = "Привет! Перед началом необходимо заполнить небольшую анкету. Нажми на кнопку ниже, чтобы перейти к заполению"
        await message.answer(text=text, reply_markup=form_button)
        # await message.answer(text="Привет! Нажми на кнопку ниже, чтобы открыть меню", reply_markup=menu_button)
        media_group = [InputMediaPhoto(
            media="AgACAgIAAxkBAAICSGZte2OWf6pYcisGeUy0cIJI_IymAAJx4DEbkQABaEvhKak6Ka0h1QEAAwIAA3kAAzUE"),
                       InputMediaPhoto(
                           media="AgACAgIAAxkBAAICTGZtffoQ_axKJc47VXKwvIsvqdYdAAJ54DEbkQABaEsxgAKJict2qQEAAwIAA3kAAzUE"),
                       InputMediaPhoto(
                           media="AgACAgIAAxkBAAICTWZtfoJP2uPl2Ip5SNPGx9MRiajeAAJ_4DEbkQABaEuTdrc85s60dAEAAwIAA3kAAzUE")
                       ]
        await message.answer_media_group(media=media_group)
    elif message.text.lower() == "главное меню бота♾️" or message.text == "/menu":
        await state.set_state(Menu.point_1)
        await message.answer(text="<b>Меню:</b>\n\nЗадания ОГЭ по математике.📝"
                                  "\n\nЗадания ЕГЭ по математике.👨🏻‍🎓"
                                  "\n\nЗадания ЕГЭ по профильной математике.🤓", reply_markup=menu_points,
                             parse_mode="html")
    elif message.text.lower() == "информация о боте❗" or message.text == "/about":
        await message.answer(text="информация о боте❗", reply_markup=link_keyboard)
    else:
        await message.answer(text="Извините я вас не понимаю выберите кнопку")









