from pyrogram import Client, filters
from config import Config

# 1. الرد على أمر /start والترحيب بالمستخدم
@Client.on_message(filters.private & filters.command("start"))
async def start_private(client, message):
    # إرسال ترحيب للمستخدم
    await message.reply_text(
        f"🙋‍♂️ **أهـلاً بـك يـا {message.from_user.mention}**\n"
        "✨ **فـي بـوت تـواصـل سـورس كـرسـتـال**\n\n"
        "📩 **أرسـل رسـالـتـك الآن وسـيـتـم الـرد عـلـيـك قـريـباً**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "👑 **الـمـطـور : أسـامـة @U_K44**"
    )
    
    # تنبيهك أنت (المطور) بدخول شخص جديد
    if message.from_user.id != Config.OWNER_ID:
        try:
            await client.send_message(
                Config.OWNER_ID,
                f"👤 **مـسـتـخـدم جـديـد دخـل لـلـبـوت:**\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"🙋‍♂️ **الاسـم:** {message.from_user.mention}\n"
                f"🆔 **الايدي:** `{message.from_user.id}`\n"
                f"✨ **يـوزر:** @{message.from_user.username if message.from_user.username else 'لا يوجد'}"
            )
        except:
            pass

# 2. نظام التواصل (إرسال واستقبال الرسائل)
@Client.on_message(filters.private & ~filters.command(["start", "help"]) & ~filters.regex("^(الاوامر|سورس|السورس)$"))
async def contact_dev(client, message):
    # إذا كنت أنت (أسامة) ترد على توجيه
    if message.from_user.id == Config.OWNER_ID:
        if message.reply_to_message and message.reply_to_message.forward_from:
            user_id = message.reply_to_message.forward_from.id
            try:
                await message.copy(user_id)
                await message.reply_text("✅ **تـم إرسـال ردك بـنـجـاح**")
            except Exception as e:
                await message.reply_text(f"❌ **فـشـل الإرسـال: {e}**")
        return

    # توجيه رسالة الشخص إليك
    try:
        await message.forward(Config.OWNER_ID)
        await message.reply_text("✨ **تـم إرسـال رسـالـتـك لـلـمـطـور أسـامـة، انـتـظـر الـرد**")
    except:
        await message.reply_text("❌ **عـذراً، فـشل إرسـال الرسالة للمطور حالياً**")
