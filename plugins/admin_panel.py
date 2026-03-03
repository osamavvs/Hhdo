from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import Config
import os

# --- لوحة التحكم الرئيسية بالأزرار ---
@Client.on_message(filters.regex("^(لوحة التحكم|التحكم|السورس)$") & filters.user(Config.OWNER_ID))
async def admin_panel(client, message):
    await message.reply_text(
        "💎 **أهلاً بك في لوحة تحكم كرستال الذكية**\n"
        "إليك أدوات السيطرة الكاملة على البوت:",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("📊 الإحصائيات", callback_data="stats"),
                InlineKeyboardButton("📢 إذاعة", callback_data="broadcast")
            ],
            [
                InlineKeyboardButton("📁 نسخة احتياطية", callback_data="backup"),
                InlineKeyboardButton("🔄 تحديث البوت", callback_data="restart")
            ],
            [
                InlineKeyboardButton("🛠 إعدادات الحماية", callback_data="protect_settings")
            ],
            [
                InlineKeyboardButton("🌐 قناة السورس", url="https://t.me/YourChannel")
            ]
        ])
    )

# --- معالج الضغط على الأزرار (Callback) ---
@Client.on_callback_query()
async def callback_handler(client, query: CallbackQuery):
    if query.from_user.id != Config.OWNER_ID:
        return await query.answer("❌ هذا الأمر للمطور فقط!", show_alert=True)

    if query.data == "stats":
        u_count = len(open("users.txt", "a+").read().split())
        g_count = len(open("groups.txt", "a+").read().split())
        await query.edit_message_text(
            f"📊 **إحصائيات سورس كرستال:**\n\n"
            f"👤 عدد المستخدمين: `{u_count}`\n"
            f"👥 عدد المجموعات: `{g_count}`",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="home")]])
        )

    elif query.data == "broadcast":
        await query.edit_message_text(
            "📢 **قسم الإذاعة:**\n\n"
            "قم بالرد على الرسالة التي تريد نشرها بكلمة `اذاعة` وسيتم إرسالها لجميع المشتركين.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="home")]])
        )

    elif query.data == "home":
        await query.edit_message_text(
            "💎 **أهلاً بك في لوحة تحكم كرستال الذكية**\n"
            "إليك أدوات السيطرة الكاملة على البوت:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📊 الإحصائيات", callback_data="stats"), InlineKeyboardButton("📢 إذاعة", callback_data="broadcast")],
                [InlineKeyboardButton("📁 نسخة احتياطية", callback_data="backup"), InlineKeyboardButton("🔄 تحديث البوت", callback_data="restart")],
                [InlineKeyboardButton("⬅️ إغلاق", callback_data="close")]
            ])
        )

    elif query.data == "close":
        await query.message.delete()
