from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, Message

# الأيدي الخاص بك يا أسامة
OWNER_ID = 5406798224

@Client.on_message(filters.private & filters.regex("^(لوحة|لوحة التحكم|المطور)$"))
async def owner_panel(client, message: Message):
    # التحقق الصارم من الأيدي
    if message.from_user.id != OWNER_ID:
        # إذا حاول شخص آخر.. البوت يتجاهله تماماً
        return 

    # أزرار الكيبورد الثابتة (تظهر لك أنت فقط)
    keyboard = ReplyKeyboardMarkup(
        [
            ["⚙️ إعدادات البوت"],
            ["📊 الإحصائيات", "📢 إذاعة عامة"],
            ["🚫 حظر مستخدم", "🔓 فك حظر"],
            ["🔄 إعادة تشغيل السورس"]
        ],
        resize_keyboard=True
    )

    await message.reply_text(
        f"👑 **أهلاً بك يا مطورنا أسامة ( {message.from_user.id} )**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🛠 **لوحة التحكم الكاملة مفعلة الآن تحت أمرك.**",
        reply_markup=keyboard
    )

# كود الإحصائيات السريع (مثال)
@Client.on_message(filters.private & filters.regex("^📊 الإحصائيات$"))
async def stats_msg(client, message: Message):
    if message.from_user.id == OWNER_ID:
        await message.reply_text("✨ **إحصائيات سورس كرستال :**\n\n👥 المجموعات: جاري الفحص..\n👤 المستخدمين: جاري الفحص..")
