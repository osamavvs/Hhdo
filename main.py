from pyrogram import Client
from config import Config

# إعداد البوت
app = Client(
    "CrystalBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins") # هذا السطر يخليك تعدل أي ملف في مجلد plugins ويشتغل تلقائياً
)

if __name__ == "__main__":
    print("💎 سورس كريستال يعمل الآن.. بانتظار تعديلاتك يا أسامة!")
    app.run()
