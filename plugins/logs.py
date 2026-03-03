from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config

# 1. إشعار دخول مستخدم جديد للخاص
@Client.on_message(filters.private & filters.command("start"))
async def start_notification(client, message: Message):
    if message.from_user.id != Config.OWNER_ID:
        log_text = (
            "👤 **مستخدِم جديد دخل للبوت!**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            f"🙋‍♂️ **الاسم:** {message.from_user.mention}\n"
            f"🆔 **الايدي:** `{message.from_user.id}`\n"
            f"✨ **اليوزر:** @{message.from_user.username if message.from_user.username else 'لا يوجد'}\n"
            "━━━━━━━━━━━━━━━━━━━━"
        )
        try:
            await client.send_message(Config.OWNER_ID, log_text)
        except:
            pass
    # هنا يكمل البوت كود الستارت الطبيعي (الأزرار والترحيب)

# 2. إشعار تفعيل البوت في مجموعة جديدة
@Client.on_message(filters.new_chat_members)
async def group_notification(client, message: Message):
    bot_id = (await client.get_me()).id
    for member in message.new_chat_members:
        if member.id == bot_id:
            # جلب رابط المجموعة إن وجد
            try:
                link = await client.export_chat_invite_link(message.chat.id)
            except:
                link = "لا يمكن جلب الرابط (البوت ليس أدمن)"

            log_text = (
                "✅ **تم تفعيل البوت في مجموعة جديدة!**\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"👥 **اسم المجموعة:** {message.chat.title}\n"
                f"🆔 **ايدي المجموعة:** `{message.chat.id}`\n"
                f"🔗 **الرابط:** {link}\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"👤 **بواسطة:** {message.from_user.mention}\n"
                f"🆔 **ايدي الشخص:** `{message.from_user.id}`\n"
                "━━━━━━━━━━━━━━━━━━━━"
            )
            try:
                await client.send_message(Config.OWNER_ID, log_text)
            except:
                pass
