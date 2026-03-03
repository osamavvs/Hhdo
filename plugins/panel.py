from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import Config

@Client.on_message(filters.regex("^(لوحه|اللوحه|لوحة التحكم)$") & filters.private)
async def smart_panel(client, message: Message):
    user_id = message.from_user.id
    
    # --- أولاً: لوحة المطور (تظهر لأسامة فقط) ---
    if user_id == Config.OWNER_ID:
        text = (
            "👑 **أهلاً بك يا مطورنا أسامة في لوحتك الخاصة**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "⚙️ **تحكم في البوت والسيرفر من هنا :**"
        )
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("📢 إذاعة عامة", callback_data="p_broadcast"),
                InlineKeyboardButton("📊 الإحصائيات", callback_data="p_stats")
            ],
            [
                InlineKeyboardButton("🚫 حظر مستخدم", callback_data="p_ban"),
                InlineKeyboardButton("🔓 فك حظر", callback_data="p_unban")
            ],
            [
                InlineKeyboardButton("🔄 ريستارت البوت", callback_data="p_restart")
            ],
            [
                InlineKeyboardButton("💎 قناة السورس", url="https://t.me/BBABB9")
            ]
        ])
        return await message.reply_text(text, reply_markup=buttons)

    # --- ثانياً: لوحة الأعضاء (تظهر لعامة المستخدمين) ---
    else:
        text = (
            f"🙋‍♂️ **أهلاً بك يا {message.from_user.mention}**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "✨ **هذه لوحة خدمات سورس كرستال :**"
        )
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🛡 أوامر البوت", callback_data="h_back"),
                InlineKeyboardButton("🎮 الألعاب", callback_data="h_games")
            ],
            [
                InlineKeyboardButton("👨‍💻 تواصل المطور", url="https://t.me/U_K44"),
                InlineKeyboardButton("💎 قناة السورس", url="https://t.me/BBABB9")
            ],
            [
                InlineKeyboardButton("➕ أضف البوت لمجموعتك", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")
            ]
        ])
        return await message.reply_text(text, reply_markup=buttons)
