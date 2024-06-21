from main import bot

async def admin(text):
    await bot.send_message(chat_id=900841184, text=text)