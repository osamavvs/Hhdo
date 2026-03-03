from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") & filters.private)
async def start_sultan(client, message):
    await message.reply_text(
        f"💎 **أهلاً بك في سورس كرستال الذكي**\n\n"
        f"👤 **المستخدم:** {message.from_user.mention}\n"
        f"⚙️ **بوت خدمات متطور يعمل بالذكاء الاصطناعي**\n\n"
        "• استخدم الأزرار بالأسفل للتنقل ↓",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🛠 أوامر البوت", callback_data="help_cmds"),
                InlineKeyboardButton("📊 الإحصائيات", callback_data="stats")
            ],
            [
                InlineKeyboardButton("👨‍💻 مطور السورس", url="https://t.me/osamavvs"),
                InlineKeyboardButton("📢 قناة التحديثات", url="https://t.me/YourChannel")
            ],
            [
                InlineKeyboardButton("➕ أضف البوت لمجموعتك", url=f"https://t.me/{client.me.username}?startgroup=true")
            ]
        ])
    )
