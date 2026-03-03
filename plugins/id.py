from pyrogram import Client, filters

@Client.on_message(filters.regex("^(ايدي|id|ID)$"))
async def get_my_id(client, message):
    await message.reply_text(f"👤 اسمك: {message.from_user.first_name}\n🆔 ايديك: `{message.from_user.id}`")

@Client.on_message(filters.regex("^(اوامر|الاوامر)$"))
async def help_list(client, message):
    await message.reply_text("💎 **أوامر كرستال المنظمة:**\n1- ايدي\n2- مرحبا\n3- سورس")
