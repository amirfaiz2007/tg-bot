from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton)

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню")]
    ]
)


link_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Телеграм", url="https://t.me/amirka000")],
        [InlineKeyboardButton(text="Сайт", url="https://sdamgia.ru/")],
        [InlineKeyboardButton(text="справочный материал", url="https://ege.sdamgia.ru/page/theory")]
    ]
)

menu_points = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Задания ОГЭ по математике.📝")],
        [KeyboardButton(text="Задания ЕГЭ по математике.👨🏻‍🎓")],
        [KeyboardButton(text="Задания ЕГЭ по профильной математике.🤓")],
        [KeyboardButton(text="кубик рандома🎲")]
    ]
)
help_points = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="главное меню бота♾️")],
        [KeyboardButton(text="информация о боте❗")],
        [KeyboardButton(text="запустить бота заново▶️")],
        [KeyboardButton(text="связь с администрацией бота👨🏽‍💻")]
    ]
)

ege = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="перейти", url="https://mathb-ege.sdamgia.ru/test?id=18985435")]
    ]
)

oge = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="перейти", url="https://math-oge.sdamgia.ru/test?id=54383187")]
    ]
)

ege_prof = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="перейти", url="https://math-ege.sdamgia.ru/test?id=76781843")]
    ]
)
form_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Перейти к анкете")]
    ]
)
