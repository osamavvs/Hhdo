from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# أمر فتح قائمة الأوامر (يدعم /help و كلمة الاوامر)
@Client.on_message(filters.command("help") | filters.regex("^الاوامر$"))
async def help_menu(client, message):
    text = (
        f"💎 **أهـلاً بـك عـزيـزي فـي أوامـر الـسـورس**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 **الـمـطـور : أسـامـة @U_K44**\n"
        f"⚙️ **قـنـاة الـسـورس : @BBABB9**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"• اضـغـط عـلـى الأزرار لـتـظـهـر لـك الأوامـر ↓"
    )
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🛡 أوامر الحماية", callback_data="h_protect"),
            InlineKeyboardButton("⚙️ أوامر المشرفين", callback_data="h_admin")
        ],
        [
            InlineKeyboardButton("🎮 أوامر التسلية", callback_data="h_fun"),
            InlineKeyboardButton("💎 أوامر السورس", callback_data="h_source")
        ],
        [
            InlineKeyboardButton("❌ إغلاق القائمة", callback_data="close_help")
        ]
    ])
    
    await message.reply_text(text, reply_markup=buttons)

# معالج الأزرار (تأكد من تغيير الـ callback_data لتجنب التعارض)
@Client.on_callback_query(filters.regex("^h_"))
async def help_callback(client, query: CallbackQuery):
    data = query.data
    
    if data == "h_protect":
        msg = "🛡 **أوامـر الـقـفـل والـفـتـح:**\n━━━━━━━━━━━━\n• قفل | فتح (الروابط)\n• قفل | فتح (التوجيه)\n• قفل | فتح (الميديا)\n• قفل | فتح (المعرفات)"
    elif data == "h_admin":
        msg = "⚙️ **أوامـر الإدارة:**\n━━━━━━━━━━━━\n• طرد (بالرد)\n• كتم (بالرد)\n• تقييد (بالرد)\n• الغاء الكتم (بالرد)"
    elif data == "h_fun":
        msg = "🎮 **أوامـر الـتـسـلـيـة:**\n━━━━━━━━━━━━\n• ايدي (معلوماتك)\n• سورس (معلومات البوت)\n• ذكاء (تحدث مع البوت)\n• الرتبة (رتبتك بالمجموعة)"
    elif data == "h_source":
        msg = "💎 **مـعـلـومـات الـسـورس:**\n━━━━━━━━━━━━\n• الـمـطور: أسـامـة @U_K44\n• الـقـناة: @BBABB9\n• الاصدار: 1.0v"

    await query.edit_message_text(
        msg,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="h_back")]])
    )

@Client.on_callback_query(filters.regex("h_back"))
async def back_callback(client, query: CallbackQuery):
    # نستخدم نفس النص والأزرار الأساسية للرجوع
    await help_menu(client, query.message)
    await query.message.delete()

@Client.on_callback_query(filters.regex("close_help"))
async def close_callback(client, query: CallbackQuery):
    await query.message.delete()
