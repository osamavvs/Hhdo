from pyrogram import Client, filters
from pyrogram.types import Message

# قائمة الأوامر بتنسيق العمدة
HELP_TEXT = """
**💎 أهلاً بك في أوامر سورس كريستال**
**━━━━━━━━━━━━━━━━━**

**⬅️ أوامر الإشراف:**
• `ايدي` : لعرض معلوماتك وآيديك
• `كشف` : بالرد لعرض معلومات العضو
• `طرد` : لطرد العضو من المجموعة

**⬅️ أوامر التسلية:**
• `نسبة حبه` : لقياس نسبة الحب (بالرد)
• `ذكاء` : لقياس نسبة الذكاء

**⬅️ أوامر المطور:**
• `تحديث` : لجلب تحديثات GitHub
• `الاحصائيات` : لعرض إحصائيات البوت

**━━━━━━━━━━━━━━━━━**
**[SOURCE CRYSTAL](https://t.me/your_channel)**
"""

@Client.on_message(filters.command(["الاوامر", "help"], "") | filters.regex("^الاوامر$"))
async def show_help(client, message: Message):
    print(f"✅ استلمت أمر الأوامر من: {message.from_user.id}") # عشان يظهر لك بالترمينال
    await message.reply_text(HELP_TEXT, disable_web_page_preview=True)

@Client.on_message(filters.command(["ايدي", "id"], "") | filters.regex("^ايدي$"))
async def get_id(client, message: Message):
    user = message.from_user
    chat = message.chat
    text = (
        f"**👤 معلوماتك يا {user.first_name}:**\n"
        f"**— الآيدي:** `{user.id}`\n"
        f"**— اليوزر:** @{user.username if user.username else 'لا يوجد'}\n"
        f"**— نوع الدردشة:** {chat.type}"
    )
    await message.reply_text(text)

@Client.on_message(filters.regex("^بوت$"))
async def bot_reply(client, message: Message):
    await message.reply_text(f"**لبيـه يا {message.from_user.mention}! اؤمرني؟ 😎**")
