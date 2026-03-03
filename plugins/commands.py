from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# لاحظ هنا نستخدم @Client وليس @app
@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(bot, message):
    text = (
        f"<b>يا هلا بك يا {message.from_user.mention} في بوت أسامة 💎</b>\n\n"
        "البوت الآن يعمل بنظام الملفات المنفصلة (Plugins) وبكامل طاقته."
    )
    
    # الأزرار الشفافة
    key = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("• المطور •", url="https://t.me/osamavvs"),
                InlineKeyboardButton("• قناة السورس •", url="https://t.me/osamavvs")
            ],
            [
                InlineKeyboardButton("• تفحص الحالة •", callback_data="check_status")
            ]
        ]
    )
    
    await message.reply_text(text, reply_markup=key, parse_mode="html")

# برمجة زر تفحص الحالة
@Client.on_callback_query(filters.regex("check_status"))
async def status_callback(bot, callback_query):
    await callback_query.answer("البوت شغال 100% ✅", show_alert=True)

# أمر "بوت" للتجربة
@Client.on_message(filters.regex("^بوت$"))
async def bot_check(bot, message):
    await message.reply_text("<b>لبيك يا عمدة، أنا أسمعك! ⚡</b>", parse_mode="html")
