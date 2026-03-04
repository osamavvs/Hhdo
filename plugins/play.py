from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command(["play", "تشغيل"]) & filters.group)
async def play_command(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("يرجى كتابة اسم الأغنية بعد الأمر (مثال: تشغيل عراقي)")
    
    query = message.text.split(None, 1)[1]
    await message.reply_text(f"🔎 جاري البحث عن: **{query}**...\nسيتم التشغيل قريباً!")
