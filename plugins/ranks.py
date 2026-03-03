from pyrogram import Client, filters
from config import Config

# أيدي المطور أسامة
SUDO_USER = 5406798224

@Client.on_message(filters.group & filters.regex("^(رتبتي|رتبتي شنو)$"))
async def get_rank(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    # التحقق من الرتبة
    if user_id == SUDO_USER:
        rank = "👑 مطور السورس (أسامة)"
    elif user_id == 5406798224: # يمكنك إضافة مطورين مساعدين هنا
        rank = "💎 مطور ثانوي"
    else:
        # فحص رتبته في المجموعة
        member = await client.get_chat_member(chat_id, user_id)
        if member.status.value == "administrator":
            rank = "🛠 أدمن المجموعة"
        elif member.status.value == "owner":
            rank = "👑 مالك المجموعة"
        else:
            rank = "👤 عضو طبيعي"

    await message.reply_text(f"🙋‍♂️ **أهلاً بك عزيزي :** {message.from_user.mention}\n✨ **رتبتك هي :** {rank}")
