from pyrogram import filters
from main import app

LOCK_LINKS = True

@app.on_message(filters.command("قفل الروابط"))
async def lock_links(client, message):
    global LOCK_LINKS
    LOCK_LINKS = True
    await message.reply("🔒 تم قفل الروابط")

@app.on_message(filters.command("فتح الروابط"))
async def unlock_links(client, message):
    global LOCK_LINKS
    LOCK_LINKS = False
    await message.reply("🔓 تم فتح الروابط")

@app.on_message(filters.group & filters.text)
async def block_links(client, message):
    if LOCK_LINKS and ("http" in message.text or "t.me" in message.text):
        await message.delete()
