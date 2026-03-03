from pyrogram import filters
from pyrogram.types import ChatPermissions
from main import app

@app.on_message(filters.command("حظر") & filters.group)
async def ban_user(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply("🚫 تم حظر العضو")
