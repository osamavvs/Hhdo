from pyrogram import Client, filters
import random

# القيم هذي اتركها صفر أو فارغة لأننا بنعبيها آلياً من الترمينال
API_ID = 0
API_HASH = ""
BOT_TOKEN = ""

app = Client("OsamaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- قسم الأوامر ---

@app.on_message(filters.command("start", ""))
async def start(client, message):
    await message.reply_text("💎 **أهلاً بك في سورس أسامة المطور!**\nتعديل مباشر من GitHub.")

@app.on_message(filters.regex("^بوت$"))
async def bot_status(client, message):
    await message.reply_text("✅ البوت متصل وشغال بآخر تحديث سحبته.")

@app.on_message(filters.regex("^ايدي$"))
async def my_id(client, message):
    await message.reply_text(f"👤 اسمك: {message.from_user.first_name}\n🆔 آيديك: `{message.from_user.id}`")

@app.on_message(filters.
