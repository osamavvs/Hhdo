from pyrogram import Client, filters
from config import Config

@Client.on_message(filters.group & filters.text)
async def omda_style(client, message):
    text = message.text
    chat_id = message.chat.id

    # قائمة أوامر العمدة (كرستال)
    if text == "م1":
        await message.reply("🛠 **أوامر الحماية والقفل :**\n━━━━━━━━━\n• قفل | فتح (الصور)\n• قفل | فتح (الروابط)\n• قفل | فتح (التوجيه)\n• قفل | فتح (التعديل)")
    
    elif text == "م2":
        await message.reply("⚙️ **أوامر الإدارة والطرد :**\n━━━━━━━━━\n• طرد (بالرد)\n• حظر (بالرد)\n• كتم (بالرد)\n• تقييد (بالرد)")

    elif text == "م3":
        await message.reply("🎮 **أوامر التسلية والألعاب :**\n━━━━━━━━━\n• سمايلات\n• كت تويت\n• لو خيروك\n• عقاب")

    elif text == "سورس" or text == "السورس":
        await message.reply(
            f"💎 **سـورس كـرسـتـال الاصـدار الاول**\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👑 **الـمـطـور : أسـامـة @{Config.OWNER_USERNAME}**\n"
            f"📢 **الـقـناة : @{Config.CH_USER}**"
        )
