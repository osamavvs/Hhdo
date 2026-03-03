from pyrogram import Client, filters
from pyrogram.types import Message

# قاعدة بيانات وهمية بسيطة (يمكنك تطويرها لـ Redis لاحقاً)
# تخزن الحالات: True يعني مقفول، False يعني مفتوح
locked_settings = {}

# --- 1. أوامر التحكم (القفل والفتح) ---
@Client.on_message(filters.group & filters.command(["قفل", "فتح"], prefixes=""))
async def lock_unlock_handler(client, message: Message):
    # التأكد أن المرسل مشرف
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not member.status in ["administrator", "creator"]:
        return await message.reply_text("⚠️ **عذراً، هذا الأمر للمشرفين فقط!**")

    cmd = message.command[0] # قفل أو فتح
    feature = message.text.split(None, 1)[1] if len(message.command) > 1 else None
    
    if not feature:
        return await message.reply_text("📝 **يرجى كتابة الأمر بشكل صحيح، مثال: قفل الروابط**")

    chat_id = message.chat.id
    if chat_id not in locked_settings:
        locked_settings[chat_id] = {}

    if cmd == "قفل":
        locked_settings[chat_id][feature] = True
        await message.reply_text(f"✔️ **تم قفل {feature} بنجاح.**")
    else:
        locked_settings[chat_id][feature] = False
        await message.reply_text(f"🔓 **تم فتح {feature} بنجاح.**")

# --- 2. تنفيذ الحماية (فحص الرسائل) ---
@Client.on_message(filters.group & ~filters.service, group=1)
async def protection_logic(client, message: Message):
    chat_id = message.chat.id
    if chat_id not in locked_settings:
        return

    settings = locked_settings[chat_id]
    
    # استثناء المشرفين من الحماية
    member = await client.get_chat_member(chat_id, message.from_user.id)
    if member.status in ["administrator", "creator"]:
        return

    # فحص الروابط
    if settings.get("الروابط") and (message.entities or message.caption_entities):
        for entity in (message.entities or message.caption_entities):
            if entity.type in ["url", "text_link"]:
                await message.delete()
                return

    # فحص المعرفات (@)
    if settings.get("المعرف") and message.text and "@" in message.text:
        await message.delete()
        return

    # فحص التوجيه (Forward)
    if settings.get("التوجيه") and message.forward_from_chat:
        await message.delete()
        return

    # فحص الصور
    if settings.get("الصور") and message.photo:
        await message.delete()
        return
