from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import Config

@Client.on_message(filters.private & filters.command("start"))
async def start_private(client, message: Message):
    user_id = message.from_user.id
    
    # 1. تصميم أزرار الكيبورد الثابتة (للمطور أسامة)
    if user_id == Config.OWNER_ID:
        keyboard = ReplyKeyboardMarkup(
            [
                ["⚙️ لوحة تحكم المطور"],
                ["📊 الإحصائيات", "📢 إذاعة"],
                ["🔄 ريستارت", "🚫 حظر مستخدم"],
                ["💎 قناة السورس"]
            ],
            resize_keyboard=True # لجعل الأزرار بحجم مناسب
        )
        welcome_text = "👑 **أهلاً بك يا مطورنا أسامة في خاص البوت.**\n✨ **لوحة التحكم ثابتة الآن أسفل الشاشة.**"
    
    # 2. تصميم أزرار الكيبورد الثابتة (للأعضاء)
    else:
        keyboard = ReplyKeyboardMarkup(
            [
                ["🛡 أوامر البوت", "🎮 الألعاب"],
                ["👨‍💻 مراسلة المطور"],
                ["💎 قناة السورس", "➕ أضف البوت"]
            ],
            resize_keyboard=True
        )
        welcome_text = f"🙋‍♂️ **أهلاً بك يا {message.from_user.mention} في بوت كرستال.**\n✨ **استخدم الأزرار أدناه للتحكم.**"

    # إرسال رسالة الترحيب مع الكيبورد الثابت
    await message.reply_text(
        welcome_text,
        reply_markup=keyboard
    )

# --- معالجة الضغط على أزرار الكيبورد ---
@Client.on_message(filters.private & filters.text)
async def handle_keyboard_buttons(client, message: Message):
    text = message.text
    
    # أوامر المطور
    if message.from_user.id == Config.OWNER_ID:
        if text == "⚙️ لوحة تحكم المطور":
            await message.reply("🛠 فتحت لك لوحة التحكم الكاملة...")
        elif text == "📢 إذاعة":
            await message.reply("ارسل الآن الرسالة التي تريد إذاعتها.")
        # أضف بقية الأوامر هنا...

    # أوامر الأعضاء
    if text == "🛡 أوامر البوت":
        from plugins.help import protect_callback
        await message.reply("🛡 **إليك قائمة أوامر الحماية :**")
    elif text == "👨‍💻 مراسلة المطور":
        await message.reply("📩 ارسل رسالتك الآن وسيتم تحويلها لأسامة.")
