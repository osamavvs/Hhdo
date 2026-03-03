from pyrogram import Client, filters

@Client.on_message(filters.regex("^الاوامر$"))
async def test_cmd(client, message):
    await message.reply_text("✅ **هلا يا أسامة! أنا شغال وأسمعك.. وش تبي نسوي؟**")

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("💎 **سورس كريستال يعمل بنجاح!**\nارسل كلمة (الاوامر) لفتح القائمة.")
