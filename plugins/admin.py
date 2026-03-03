cat << 'EOF' > ~/Hhdo/plugins/admin.py
from pyrogram import Client, filters

@Client.on_message(filters.command("الاوامر", "") | filters.regex("^الاوامر$"))
async def commands(client, message):
    await message.reply_text("💎 **أهلاً بك يا عمدة في قائمة الأوامر:**\n\n• `ايدي` : لعرض آيديك\n• `بوت` : للتأكد من التشغيل")

@Client.on_message(filters.command("ايدي", "") | filters.regex("^ايدي$"))
async def my_id(client, message):
    await message.reply_text(f"✨ **آيديك هو:** `{message.from_user.id}`")

@Client.on_message(filters.regex("^بوت$"))
async def bot_test(client, message):
    await message.reply_text("✅ **لبيـه! البوت شغال وعال العال.**")
EOF
