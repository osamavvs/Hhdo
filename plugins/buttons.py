from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# نستخدم Client هنا بدلاً من app عشان يشتغل مع المين
@Client.on_message(filters.command("start") & filters.private)
async def start_private(bot, message):
    text = f"<b>أهلاً بك يا {message.from_user.mention} 💎</b>\n\nالآن البوت يقرأ من ملفات منفصلة!"
    
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("• قناة المطور •", url="https://t.me/osamavvs")],
            [InlineKeyboardButton("• تجربة زر •", callback_data="test_btn")]
        ]
    )
    await message.reply_text(text, reply_markup=reply_markup, parse_mode="html")

@Client.on_callback_query(filters.regex("test_btn"))
async def test_callback(bot, callback_query):
    await callback_query.answer("تم تشغيل الزر بنجاح من داخل ملف الـ Plugins! ✅", show_alert=True)
