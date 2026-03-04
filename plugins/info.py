from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("id"))
async def get_id(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "غير معروف"
    await message.reply_text(
        f"🆔 آيدي الدردشة: `{chat_id}`\n"
        f"👤 آيديك: `{user_id}`"
    )
