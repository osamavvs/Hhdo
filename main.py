from pyrogram import Client

# تأكد أن السطر التالي يحتوي على plugins=dict(root="plugins")
app = Client(
    "CrystalBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins") # هذا هو السطر الأهم
)
