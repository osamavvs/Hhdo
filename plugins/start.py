
from pyrogram import filters
from pyrogram.types import Message
from core.bot import app

@app.on_message(filters.private & filters.text)
async def start_handler(_, message: Message):
    await message.reply(
        "🎵 اهلا بك في بوت الميوزك\n\n"
        "اكتب في الكروب:\n"
        "تشغيل + اسم الاغنية"
    )
