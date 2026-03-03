from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import Config

# يوزر القناة (بدون @)
CH_USER = "BBABB9"

# فحص الرسائل التي تحتوي على أوامر فقط (تبدأ بـ / أو كلمات محددة)
@Client.on_message(filters.group & (filters.command(["start", "help", "id", "source"]) | filters.regex("^(الاوامر|سورس|ايدي|رتبتي|م1|م2|م3|ك|كشف)$")), group=-1)
async def must_join_commands(client, message: Message):
    # استثناء المطور (أسامة) من الفحص
    if message.from_user.id == Config.OWNER_ID:
        return

    try:
        # فحص الانضمام للقناة
        await client.get_chat_member(CH_USER, message.from_user.id)
    except UserNotParticipant:
        # إذا لم يكن مشتركاً، تظهر رسالة التنبيه
        link = f"https://t.me/{CH_USER}"
        await message.reply_text(
            f"⚠️ **عـذراً عـزيـزي {message.from_user.mention}**\n\n"
            f"❌ **لا يمكنك استخدام أوامر البوت إلا بعد الاشتراك في القناة**\n"
            f"💎 **اشترك في القناة ثم أعد محاولة الأمر**\n"
            f"━━━━━━━━━━━━━━━━━━━━",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 اضـغـط هـنـا لـلاشـتـراك 💎", url=link)]
            ])
        )
        # إيقاف تنفيذ الأمر (هذا يمنع البوت من الرد على الأمر الأصلي)
        message.stop_propagation()
    except Exception as e:
        print(f"Error in Must Join: {e}")

# في الخاص (الاشتراك إجباري لكل شيء لضمان التواصل)
@Client.on_message(filters.private & ~filters.me, group=-1)
async def must_join_private(client, message: Message):
    if message.from_user.id == Config.OWNER_ID:
        return
    try:
        await client.get_chat_member(CH_USER, message.from_user.id)
    except UserNotParticipant:
        link = f"https://t.me/{CH_USER}"
        await message.reply_text(
            "🙋‍♂️ **أهلاً بك في بوت التواصل**\n\n"
            "⚠️ **عليك الاشتراك في قناة السورس أولاً للمتابعة:**\n"
            f"🔗 @{CH_USER}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 اشترك الآن 💎", url=link)]
            ])
        )
        message.stop_propagation()
