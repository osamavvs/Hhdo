from pyrogram import Client, filters
from config import Config

# استقبال الرسائل في الخاص وتوجيهها للمطور
@Client.on_message(filters.private & ~filters.command(["start", "help", "سورس", "الاوامر"]))
async def contact_dev(client, message):
    # إذا كان المرسل هو المطور وتريد الرد على شخص
    if message.from_user.id == Config.OWNER_ID:
        if message.reply_to_message and message.reply_to_message.forward_from:
            user_id = message.reply_to_message.forward_from.id
            try:
                await message.copy(user_id)
                await message.reply_text("✅ **تـم إرسـال ردك إلـى الـمـسـتـخـدم بـنـجـاح**")
            except Exception as e:
                await message.reply_text(f"❌ **فـشـل الإرسـال: {e}**")
        return

    # توجيه رسالة المستخدم للمطور
    try:
        await message.forward(Config.OWNER_ID)
        await message.reply_text(
            "🙋‍♂️ **أهـلاً بـك عـزيـزي فـي قـسـم الـتـواصـل**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "✨ **تـم إرسـال رسـالـتـك إلـى الـمـطـور أسـامـة**\n"
            "⏳ **يـرجـى الانـتـظـار لـحـيـن الـرد عـلـيـك**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💎 **بـواسطـة سـورس كـرسـتـال**"
        )
    except Exception as e:
        await message.reply_text("❌ **عـذراً، هـناك مـشـكـلـة في الـتـواصـل حـالـيـاً**")

# تنبيه المطور عند دخول شخص جديد للتواصل
@Client.on_message(filters.private & filters.command("start"))
async def start_notify(client, message):
    if message.from_user.id != Config.OWNER_ID:
        await client.send_message(
            Config.OWNER_ID,
            f"👤 **مـسـتـخـدم جـديـد دخـل لـلـبـوت:**\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🙋‍♂️ **الاسـم:** {message.from_user.mention}\n"
            f"🆔 **الايدي:** `{message.from_user.id}`\n"
            f"✨ **يـوزر:** @{message.from_user.username if message.from_user.username else 'لا يوجد'}"
        )
