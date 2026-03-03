from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, Message
from config import Config

# 1. فلتر خاص للتحقق أنك "أسامة" المطور
@Client.on_message(filters.private & filters.regex("^(لوحة التحكم|الاعدادات)$"))
async def owner_only_panel(client, message: Message):
    # إذا كان الشخص ليس أسامة (المطور) لا يستجيب البوت نهائياً
    if message.from_user.id != Config.OWNER_ID:
        return 

    # أزرار التحكم الخاصة بك (تظهر لك فقط)
    keyboard = ReplyKeyboardMarkup(
        [
            ["📢 إذاعة عامة", "📊 الإحصائيات"],
            ["🚫 حظر مستخدم", "🔓 فك حظر"],
            ["🔄 إعادة تشغيل البوت"],
            ["❌ إغلاق اللوحة"]
        ],
        resize_keyboard=True
    )

    await message.reply_text(
        "👑 **أهلاً بك يا مطورنا أسامة.**\n"
        "⚙️ **لوحة التحكم الحصرية مفعلة الآن بين يديك.**",
        reply_markup=keyboard
    )

# 2. إخفاء اللوحة عند الضغط على إغلاق
@Client.on_message(filters.private & filters.regex("^❌ إغلاق اللوحة$"))
async def close_panel(client, message: Message):
    if message.from_user.id == Config.OWNER_ID:
        from pyrogram.types import ReplyKeyboardRemove
        await message.reply_text("✅ تم إغلاق لوحة التحكم.", reply_markup=ReplyKeyboardRemove())
