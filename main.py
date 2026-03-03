from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# البيانات سيتم ملؤها تلقائياً بواسطة السيرفر (أمر التحديث)
API_ID = 0
API_HASH = ""
BOT_TOKEN = ""

app = Client("OsamaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_private(client, message):
    # تنسيق الرسالة بشكل مرتب
    text = (
        f"<b>مرحباً بك يا {message.from_user.mention} 💎</b>\n\n"
        "أنا بوت الخدمة الخاص بك، أعمل بكل طاقة وسرعة.\n"
        "إليك الخيارات المتاحة حالياً:"
    )
    
    # إضافة أزرار شفافة (Inline Buttons)
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("قناة المطور 📣", url="https://t.me/osamavvs"),
                InlineKeyboardButton("الدعم الفني 🛠️", url="https://t.me/osamavvs")
            ],
            [
                InlineKeyboardButton("معلومات البوت ℹ️", callback_data="bot_info")
            ]
        ]
    )
    
    await message.reply_text(text, reply_markup=reply_markup, parse_mode="html")

@app.on_callback_query(filters.regex("bot_info"))
async def info_callback(client, callback_query):
    await callback_query.answer("هذا البوت يعمل بنظام Pyrogram 2.0", show_alert=True)

@app.on_message(filters.regex("^بوت$"))
async def bot_status(client, message):
    await message.reply_text("<b>لبيك يا عمدة، أنا متصل وجاهز! ✅</b>", parse_mode="html")

app.run()
