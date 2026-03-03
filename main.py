from pyrogram import Client
from config import Config

# إعداد المحرك لقراءة المجلدات تلقائياً
bot = Client(
    "Crystal",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins") # هذا هو السطر اللي يخلي البوت يقرأ ملفات الحماية والترحيب
)

print("--- 💎 سورس كرستال (النظام المنظم) يعمل الآن بنجاح ---")
bot.run()
