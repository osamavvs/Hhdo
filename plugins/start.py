from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await message.reply_text(f"💎 أهلاً بك في **سورس كرستال** المنظم!\nاستخدم كلمة 'اوامر' لرؤية ما يمكنني فعله.")

@Client.on_message(filters.regex("^(مرحبا|هلا|هلو)$") & filters.private)
async def hello_text(client, message):
    await message.reply_text("يا هلا بك في عالم الكرستال! ✨")
