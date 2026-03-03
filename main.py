from pyrogram import Client, filters

# سيتم ملؤها بواسطة السيرفر
API_ID = 0
API_HASH = ""
BOT_TOKEN = ""

app = Client("OsamaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(f"هلا بك يا {message.from_user.first_name} في بوت أسامة!")

@app.on_message(filters.regex("^بوت$"))
async def bot_status(client, message):
    await message.reply_text("💎 لبيك يا عمدة، أنا متصل.")

app.run()
