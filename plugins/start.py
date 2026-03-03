from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main import app

@app.on_message(filters.command("start"))
async def start(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚙️ الاعدادات", callback_data="settings")],
        [InlineKeyboardButton("📖 الاوامر", callback_data="help")]
    ])

    await message.reply_text(
        "💎 اهلاً بك في سورس الحماية\n"
        "اختر من الازرار بالاسفل 👇",
        reply_markup=buttons
    )
