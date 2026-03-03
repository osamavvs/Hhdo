from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import Config

# يوزر القناة بدون @
CH_USER = "BBABB9"

# قائمة الكلمات والأوامر المبرمجة في البوت
BOT_ACTIONS = [
    "الاوامر", "سورس", "السورس", "رتبتي", "رتبة", "رتبته", "ايدي", "ايديتي", "كشف", "ك",
    "م1", "م2", "م3", "م4", "م5", "م6", "م7", "م8", "م9", "م المطور",
    "قفل", "فتح", "تفعيل", "تعطيل", "حماية", "الالعاب", "تواصل"
]

@Client.on_message(filters.group & ~filters.service, group=-1)
async def smart_must_join(client, message: Message):
    # 1. استثناء المطور أسامة
    if message.from_user.id == Config.OWNER_ID:
        return

    if not message.text:
        return

    text = message.text.strip()
    is_bot_command = False

    # 2. التحقق هل الرسالة "أمر مبرمج" (مع استثناء /start)
    if text.startswith("/") and not text.startswith("/start"):
        is_bot_command = True
    
    elif any(word in text for word in BOT_ACTIONS):
        is_bot_command = True

    # 3. إذا كان "أمر للبوت" نفحص الاشتراك
    if is_bot_command:
        try:
            await client.get_chat_member(CH_USER, message.from_user.id)
        except UserNotParticipant:
            await message.reply_text(
                f"⚠️ **عـذراً يـا {message.from_user.mention}**\n\n"
                f"❌ **هذا الأمر من مميزات البوت الخاصة**\n"
                f"💎 **للقيام بذلك، يجب عليك الاشتراك في القناة أولاً**\n"
                f"━━━━━━━━━━━━━━━━━━━━",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("💎 اضـغـط هـنـا لـلاشـتـراك 💎", url=f"https://t.me/{CH_USER}")]
                ])
            )
            message.stop_propagation()
        except Exception:
            pass

# في الخاص يبقى الاشتراك إجباري (بما في ذلك /start لتفعيل البوت)
@Client.on_message(filters.private & ~filters.command("start"), group=-1)
async def private_must_join(client, message: Message):
    if message.from_user.id == Config.OWNER_ID:
        return
    try:
        await client.get_chat_member(CH_USER, message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
            "⚠️ **عـزيـزي، البوت لا يعمل في الخاص إلا بعد الاشتراك بالقناة!**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💎 اشترك الآن", url=f"https://t.me/{CH_USER}")]])
        )
        message.stop_propagation()
