from pyrogram import Client, filters
from config import Config
import asyncio

@Client.on_message((filters.regex(r"https?://[^\s]+") | filters.forwarded) & filters.group)
async def group_protector(client, message):
    if message.from_user.id == Config.OWNER_ID:
        return
    try:
        await message.delete()
        warn = await message.reply_text(f"⚠️ {message.from_user.mention} ممنوع الروابط والتوجيه هنا!")
        await asyncio.sleep(3)
        await warn.delete()
    except:
        pass
