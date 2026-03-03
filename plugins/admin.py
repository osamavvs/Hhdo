from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from config import Config

# أمر الطرد (طرد + ايدي الشخص أو بالرد عليه)
@Client.on_message(filters.command("طرد") & filters.group)
async def ban_user(client, message):
    # التأكد أن الشخص الذي يرسل الأمر هو المطور أو مشرف
    if message.from_user.id != Config.OWNER_ID:
        return await message.reply_text("❌ هذا الأمر للمطور فقط!")
    
    user = message.reply_to_message.from_user if message.reply_to_message else None
    if not user:
        return await message.reply_text("⚠️ يجب الرد على رسالة الشخص لطره!")
    
    try:
        await client.ban_chat_member(message.chat.id, user.id)
        await message.reply_text(f"👤 العضو {user.mention} طار من المجموعة! ✈️")
    except Exception as e:
        await message.reply_text(f"❌ فشل الطرد: {e}")

# أمر الكتم (تقييد العضو من الكتابة)
@Client.on_message(filters.command("كتم") & filters.group)
async def mute_user(client, message):
    if message.from_user.id != Config.OWNER_ID:
        return
    
    user = message.reply_to_message.from_user if message.reply_to_message else None
    if not user:
        return await message.reply_text("⚠️ رد على رسالته لكتمه!")
    
    try:
        await client.restrict_chat_member(message.chat.id, user.id, ChatPermissions(can_send_messages=False))
        await message.reply_text(f"🤐 تم كتم {user.mention} بنجاح.")
    except Exception as e:
        await message.reply_text(f"❌ خطأ: {e}")
