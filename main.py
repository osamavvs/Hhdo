from pyrogram import Client, filters
from config import Config

app = Client("GiantBot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(f"أهلاً بك يا {message.from_user.mention}\nهذا السورس الخاص بي تم رفعه بنجاح!")

print("البوت يعمل...")
app.run()
