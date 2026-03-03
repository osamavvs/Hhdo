import os
import sys
from pyrogram import Client, filters

@Client.on_message(filters.command("تحديث") & filters.me)
async def update_bot(client, message):
    msg = await message.reply("🔄 **جاري سحب التعديلات من GitHub...**")
    try:
        os.system("git pull")
        await msg.edit("✅ **تم سحب التعديلات! جاري إعادة التشغيل...**")
        # إعادة تشغيل العملية بالكامل
        os.execl(sys.executable, sys.executable, "main.py")
    except Exception as e:
        await msg.edit(f"❌ **حدث خطأ أثناء التحديث:**\n`{e}`")
