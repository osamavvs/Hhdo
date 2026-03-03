from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

@Client.on_message(filters.regex("^(لوحة التحكم|التحكم)$") & filters.user(Config.OWNER_ID))
async def sultan_panel(client, message):
    await message.reply_text(
        "🛠 **لوحة تحكم المطور (سورس كرستال)**\n"
        "——————————————————\n"
        "تحكم في جميع وظائف البوت من هنا:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📢 إذاعة عامة", callback_data="broadcast"), InlineKeyboardButton("🔄 إعادة تشغيل", callback_data="restart")],
            [InlineKeyboardButton("👥 قائمة المجموعات", callback_data="groups_list"), InlineKeyboardButton("👤 قائمة المستخدمين", callback_data="users_list")],
            [InlineKeyboardButton("🚫 حظر مستخدم", callback_data="ban_user"), InlineKeyboardButton("✅ إلغاء حظر", callback_data="unban_user")],
            [InlineKeyboardButton("⚙️ إعدادات الحماية", callback_data="guard_settings")],
            [InlineKeyboardButton("❌ إغلاق اللوحة", callback_data="close")]
        ])
    )
