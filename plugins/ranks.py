from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config

@Client.on_message(filters.group & filters.regex("^(رتبتي|الرتبة|رتبة)$"))
async def get_rank(client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    # 1. التحقق إذا كان هو مطور السورس (أسامة)
    if user_id == Config.OWNER_ID:
        rank = "👑 مـطـور الـسـورس"
    else:
        # 2. جلب معلومات العضو من تليجرام
        member = await client.get_chat_member(chat_id, user_id)
        
        if member.status == "creator":
            rank = "💎 مـالـك الـمـجـمـوعـة"
        elif member.status == "administrator":
            rank = "🛠 مـشـرف الـمـجـمـوعـة"
        else:
            rank = "👤 عـضـو مـمـيـز"

    # إرسال الرتبة بتصميم فخم
    await message.reply_text(
        f"🙋‍♂️ **أهـلاً بـك يـا {message.from_user.mention}**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"✨ **رتبـتـك هـي :** {rank}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"💎 **بـواسـطـة سـورس كـرسـتـال**"
    )

# أمر إضافي لعرض رتبة شخص بالرد عليه
@Client.on_message(filters.group & filters.regex("^رتبته$") & filters.reply)
async def get_reply_rank(client, message: Message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.mention

    if user_id == Config.OWNER_ID:
        rank = "👑 مـطـور الـسـورس"
    else:
        member = await client.get_chat_member(chat_id, user_id)
        if member.status == "creator":
            rank = "💎 مـالـك الـمـجـمـوعـة"
        elif member.status == "administrator":
            rank = "🛠 مـشـرف الـمـجـمـوعـة"
        else:
            rank = "👤 عـضـو فـي الـمـجـمـوعـة"

    await message.reply_text(f"✨ **رتبـة الشخص {user_name} هي :**\n{rank}")
