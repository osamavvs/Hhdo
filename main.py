from pyrogram import Client, filters

# --- بياناتك الشخصية ---
API_ID = 24752047
API_HASH = "5b8a468627791bdd36a8c361913b0b72"
BOT_TOKEN = "8721155986:AAHdipR_Xg6YUebhq_FWU3_oeHjyNdePT_c"

app = Client(
    "OsamaBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# --- الأوامر ---

@app.on_message(filters.command("start", ""))
async def start(client, message):
    await message.reply_text("💎 **أهلاً بك في سورس أسامة المطور!**\nالسورس جاهز للعمل الآن.")

@app.on_message(filters.regex("^بوت$"))
async def bot_status(client, message):
    await message.reply_text("✅ البوت متصل وشغال عال العال.")

@app.on_message(filters.regex("^ايدي$"))
async def get_id(client, message):
    await message.reply_text(f"✨ آيديك هو: `{message.from_user.id}`")

# تشغيل البوت
if __name__ == "__main__":
    print("🚀 البوت بدأ العمل...")
    app.run()
