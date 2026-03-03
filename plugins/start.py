from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") & filters.private)
async def start_sultan_pro(client, message):
    text = (
        f"🙋‍♂️ **أهـلاً بـك يـا عـزيـزي** {message.from_user.mention}\n\n"
        f"💠 **فـي بـوت سـورس كـرسـتـال الـمتـطـور**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"💎 **مـهـمـة الـبـوت : حـمـايـة وتـطـويـر الـمـجـمـوعـات**\n"
        f"⚡ **سـرعـة الـرد : فـائـقـة**\n"
        f"👤 **الـمـطـور : أســامــة الـعـمـده**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"• اسـتـخدم الأزرار بالأسـفل لـلتـنـقـل بـين الأقسـام ↓"
    )
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🛠 أوامر البوت", callback_data="help_cmds"),
            InlineKeyboardButton("📊 إحصائياتي", callback_data="stats")
        ],
        [
            InlineKeyboardButton("👨‍💻 الـمـطـور", url="https://t.me/U_K44"),
            InlineKeyboardButton("📢 قـنـاة الـسـورس", url="https://t.me/BBABB9")
        ],
        [
            InlineKeyboardButton("➕ أضف البوت لمجموعتك", url=f"https://t.me/{client.me.username}?startgroup=true")
        ]
    ])
    
    await message.reply_text(text, reply_markup=buttons)
