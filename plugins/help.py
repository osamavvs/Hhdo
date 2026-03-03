from pyrogram import filters
from main import app

@app.on_message(filters.command("الاوامر") & filters.group)
async def help_cmd(client, message):
    text = """
📖 اوامر الادمن:

🚫 حظر (بالرد)
🔓 فتح الروابط
🔒 قفل الروابط
⚠️ تحذير (بالرد)

💎 المطور: @username
"""
    await message.reply(text)
