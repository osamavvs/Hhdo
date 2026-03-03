from pyrogram import Client, filters
import random

# اترك هذه القيم كما هي، سنملأها من السيرفر تلقائياً
API_ID = 0
API_HASH = ""
BOT_TOKEN = ""

app = Client("OsamaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start", ""))
async def start(client, message):
    await message.reply_text("💎 أهلاً بك في سورس أسامة المحدث من GitHub!")

@app.on_message(filters.regex("^بوت$"))
async def bot_status(client, message):
    await message.reply_text("✅ البوت متصل وشغال بآخر تحديث من GitHub.")

@app.on_message(filters.regex("^حظ$"))
async def luck(client, message):
    await message.reply_text(random.choice(["حظك عسل 🍯", "حظك نار 🔥", "حظك وسط ⚖️"]))

# أضف أي أوامر تريدها هنا في GitHub مستقبلاً
app.run()
