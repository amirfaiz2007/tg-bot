import asyncio
import common_handler
from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from antiflood import AntifloodMiddleware
from handlers import about, help, start, form
from config_reader import config
from database import start_db

bot = Bot(config.bot_token.get_secret_value())
dp = Dispatcher()


async def main():
    await start_db()
    dp.message.middleware(AntifloodMiddleware())
    dp.include_routers(
        start.router,
        common_handler.router,
        form.router,
        help.router,
        about.router,
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


