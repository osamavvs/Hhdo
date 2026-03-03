from pyrogram import Client

# البيانات سيتم ملؤها تلقائياً بواسطة السيرفر
API_ID = 24752047
API_HASH = "5b8a468627791bdd36a8c361913b0b72"
BOT_TOKEN = "8721155986:AAHdipR_Xg6YUebhq_FWU3_oeHjyNdePT_c"

class Bot(Client):
    def __init__(self):
        super().__init__(
            "OsamaBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins") # هذا يخلي البوت يقرأ كل شي داخل مجلد plugins
        )

    async def start(self):
        await super().start()
        print("🚀 البوت اشتغل وبدأ يقرأ ملفات الأزرار من plugins...")

    async def stop(self, *args):
        await super().stop()

if __name__ == "__main__":
    Bot().run()
