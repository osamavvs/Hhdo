from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, Message
from config import Config

@Client.on_message(filters.private & filters.command("start"))
async def start_private(client, message: Message):
    user_id = message.from_user.id
    
    # --- 1. إرسال إشعار لك (أسامة) بدخول شخص جديد ---
    if user_id != Config.OWNER_ID:
        try:
            log_text = (
                "👤 **عضو جديد دخل لبوتك!**\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"🙋‍♂️ **الاسم:** {message.from_user.mention}\n"
                f"🆔 **الايدي:** `{user_id}`\n"
                f"✨ **اليوزر:** @{message.from_user.username if message.from_user.username else 'لا يوجد'}"
            )
            await client.send_message(Config.OWNER_ID, log_text)
        except:
            pass

    # --- 2. عرض الأزرار الثابتة (الكيبورد) ---
    if user_id == Config.OWNER_ID:
        keyboard = ReplyKeyboardMarkup(
            [["⚙️ لوحة التحكم"], ["📊 الإحصائيات", "📢 إذاعة"], ["🔄 ريستارت"]],
            resize_keyboard=True
        )
        welcome = "👑 **أهلاً بك يا مطورنا أسامة في لوحتك.**"
    else:
        keyboard = ReplyKeyboardMarkup(
            [["🛡 أوامر البوت", "🎮 الألعاب"], ["💎 قناة السورس", "➕ أضف البوت"]],
            resize_keyboard=True
        )
        welcome = f"🙋‍♂️ **أهلاً بك يا {message.from_user.mention} في بوت كرستال.**"

    await message.reply_text(welcome, reply_markup=keyboard)

# --- 3. منع تحويل الرسائل (إلغاء التواصل) ---
@Client.on_message(filters.private & ~filters.command("start") & ~filters.me)
async def disable_contact(client, message: Message):
    # إذا لم تكن الرسالة أمراً، البوت لن يفعل شيئاً ولن يحولها للمطور
    pass
