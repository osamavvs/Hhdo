cat <<EOF > plugins/owner_panel.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

@Client.on_message(filters.command(["لوحه", "لوحة", "المطور"]) & filters.user(Config.OWNER_ID))
async def owner_panel(client, message):
    text = (
        "💎 **أهلاً بك يا مطورنا أسامة في لوحة التحكم**\n\n"
        "يمكنك إدارة سورس كرستال من خلال الأزرار أدناه:"
    )
    buttons = [
        [
            InlineKeyboardButton("📢 إذاعة للكل", callback_data="broadcast"),
            InlineKeyboardButton("📊 الإحصائيات", callback_data="stats")
        ],
        [
            InlineKeyboardButton("🛡 قفل/فتح البوت", callback_data="toggle_bot"),
            InlineKeyboardButton("📝 نسخة احتياطية", callback_data="backup")
        ],
        [
            InlineKeyboardButton("👤 المطور", url=f"t.me/{Config.OWNER_USERNAME}")
        ]
    ]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex("^(broadcast|stats|toggle_bot|backup)$"))
async def callback_handler(client, callback_query):
    # رد سريع للأزرار (قيد التطوير حالياً)
    await callback_query.answer("🛠 هذه الميزة قيد التفعيل في التحديث القادم يا أسامة", show_alert=True)
EOF
