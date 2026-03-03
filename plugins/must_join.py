from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import Config

# يوزر القناة (تأكد أنه نفس اللي في الكونسول)
CH_USER = "BBABB9"

@Client.on_message(filters.group | filters.private, group=-1)
async def must_join_func(client, message: Message):
    # استثناء المطور (أسامة) من الفحص
    if message.from_user.id == Config.OWNER_ID:
        return

    try:
        # فحص إذا كان العضو مشترك في القناة
        await client.get_chat_member(CH_USER, message.from_user.id)
    except UserNotParticipant:
        # إذا لم يكن مشتركاً، تظهر له هذه الرسالة مع رابط القناة
        link = f"https://t.me/{CH_USER}"
        await message.reply_text(
            f"⚠️ **عـذراً عـزيـزي {message.from_user.mention}**\n\n"
            f"❌ **لا يمكنك استخدام البوت إلا بعد الاشتراك في القناة**\n"
            f"💎 **اشترك ثم ارسل ( /start ) لتفعيل البوت**\n"
            f"━━━━━━━━━━━━━━━━━━━━",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💎 اضـغـط هـنـا لـلاشـتـراك 💎", url=link)]
            ])
        )
        # إيقاف معالجة بقية الأوامر
        message.stop_propagation()
    except Exception as e:
        # في حال وجود خطأ تقني (مثل أن البوت ليس مشرفاً في القناة)
        print(f"Error in Must Join: {e}")
