from pyrogram import Client, filters
from config import Config

# هذا الفلتر يمسك كل رسايل الخاص اللي مو "أمر" (Command)
# ويمنعها من الانتقال لأي ملف ثاني (يعني يقتلها هنا)
@Client.on_message(filters.private & ~filters.command(["start", "help", "لوحه"]) & ~filters.me)
async def stop_all_forwards(client, message):
    # إذا الشخص مو المطور أسامة، البوت ما راح يسوي Forward لأي رسالة
    if message.from_user.id != Config.OWNER_ID:
        # يمكنك إضافة رد تلقائي بسيط هنا إذا أردت، أو تركه فارغاً تماماً
        # await message.reply("⚠️ التواصل مع المطور مغلق حالياً.")
        message.stop_propagation() # أهم سطر لقتل عملية التواصل
