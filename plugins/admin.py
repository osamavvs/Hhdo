from pyrogram import Client, filters

@Client.on_message(filters.command("id") & filters.private)
async def get_id(bot, message):
    await message.reply_text(f"ايديك هو: <code>{message.from_user.id}</code>", parse_mode="html")
