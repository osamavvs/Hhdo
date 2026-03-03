from pyrogram import Client, filters
from pyrogram.types import Message
import time

# --- أوامر المطور (استبدل 123456789 بآيديك) ---
OWNER_ID = 8074717568

@Client.on_message(filters.command("الاوامر") & filters.private)
async def commands_list(client, message):
    text = (
        "** تـم فـتـح قـائـمـة الأوامـر 💎**\n"
        "**━━━━━━━━━━━━━━━━━**\n"
        "**• 「 أوامـر الـحـمـايـة 」**\n"
        "**—** `قفل` + (الصور، الروابط، التوجيه)\n"
        "**—** `فتح` + (الصور، الروابط، التوجيه)\n\n"
        "**• 「 أوامـر الإدارة 」**\n"
        "**—** `طرد` (بالرد)\n"
        "**—** `كتم` (بالرد)\n"
        "**—** `تثبيت` (بالرد)\n\n"
        "**• 「 أوامـر الـمـعـلـومـات 」**\n"
        "**—** `ايدي` : كشف هويتك\n"
        "**—** `كشف` : معلومات العضو (بالرد)\n"
        "**━━━━━━━━━━━━━━━━━**\n"
        "**[SOUCRE CRYSTAL](https://t.me/your_channel)**"
    )
    await message.reply_text(text, disable_web_page_preview=True)

@Client.on_message(filters.command("ايدي") & filters.group)
async def id_command(client, message):
    user = message.from_user
    chat = message.chat
    await message.reply_text(
        f"** تـم كـشـف هـويـتـك بـنـجـاح 🕵️‍♂️**\n"
        f"**━━━━━━━━━━━━━━━━━**\n"
        f"**• اسـمـك :** {user.mention}\n"
        f"**• آيـديـك :** `{user.id}`\n"
        f"**• رتـبـتـك :** {'الـمـطـور 👑' if user.id == OWNER_ID else 'عـضـو 👤'}\n"
        f"**• آيـدي الـكـروب :** `{chat.id}`\n"
        f"**━━━━━━━━━━━━━━━━━**"
    )

@Client.on_message(filters.command("كتم") & filters.user(OWNER_ID) & filters.reply)
async def mute_user(client, message):
    await message.chat.restrict_member(message.reply_to_message.from_user.id, permissions=None)
    await message.reply_text(f"**✅ تـم كـتـم الـعـضـو :** {message.reply_to_message.from_user.mention}\n**بـأمر الـعـمـدة! 🤫**")
