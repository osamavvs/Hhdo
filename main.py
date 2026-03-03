from pyrogram import Client, filters

# اتركها كما هي، السيرفر سيقوم بملئها
API_ID = 0
API_HASH = ""
BOT_TOKEN = ""

app = Client("OsamaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start", ""))
async def start(client, message):
    await message.reply_text("✅ تم التحديث بنجاح من GitHub والبوت شغال!")

@app.on_message(filters.regex("^بوت$"))
async def bot_status(client, message):
    await message.reply_text("💎 لبيك يا عمدة، أنا متصل.")

app.run()
