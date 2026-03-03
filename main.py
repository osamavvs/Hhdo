from pyrogram import Client, filters
import random

API_ID = 0
API_HASH = ""
BOT_TOKEN = ""

app = Client("OsamaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start", ""))
async def start(client, message):
    await message.reply_text("💎 أهلاً بك في سورس أسامة المحدث من GitHub!")

@app.on_message(filters.regex("^بوت$"))
async def bot_status(client, message):
    await message.reply_text("✅ البوت شغال وعال العال يا عمدة.")

@app.on_message(filters.regex("^ايدي$"))
async def my_id(client, message):
    await message.reply_text(f"🆔 آيديك: `{message.from_user.id}`")

app.run()
