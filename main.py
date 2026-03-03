from pyrogram import Client
from config import Config
import os

# إنشاء كائن البوت
app = Client(
    "CrystalBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    print("🚀 جاري فحص الملفات...")
    if not os.path.exists("plugins"):
        os.makedirs("plugins")
    print(f"✅ تم العثور على المجلدات. جاري تشغيل البوت...")
    app.run()
