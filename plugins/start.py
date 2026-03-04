from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start") & filters.private)
async def start_private(client: Client, message: Message):
    await message.reply_text(
        f"أهلاً بك يا {message.from_user.mention}..\n\n"
        "أنا بوت تشغيل الموسيقى في المكالمات الصوتية.\n"
        "أضفني لمجموعتك وارفعني مشرفاً للبدء!"
    )

@Client.on_message(filters.command("start") & filters.group)
async def start_group(client: Client, message: Message):
    await message.reply_text("البوت يعمل بنجاح في المجموعة! ✅")
