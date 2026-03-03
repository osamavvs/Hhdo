from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(filters.command("start") & filters.private)
async def start_private(client, message):
    text = f"<b>أهلاً بك يا {message.from_user.mention} 💎</b>\n\nاختر من الأزرار بالأسفل:"
    
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("• قسم الملفات •", callback_data="files_menu")],
            [InlineKeyboardButton("• المطور •", url="https://t.me/osamavvs")]
        ]
    )
    await message.reply_text(text, reply_markup=reply_markup, parse_mode="html")

@app.on_callback_query(filters.regex("files_menu"))
async def files_callback(client, callback_query):
    await callback_query.answer("هذه الأوامر تعمل من ملفات منفصلة! ✅", show_alert=True)
