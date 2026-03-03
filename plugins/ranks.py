cat <<EOF > plugins/ranks.py
from pyrogram import Client, filters
from config import Config
import sqlite3
import random

# الاتصال بقاعدة البيانات وإنشاء الجداول
db = sqlite3.connect("bot_database.db", check_same_thread=False)
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, msgs INTEGER DEFAULT 0)")
db.commit()

@Client.on_message(filters.group | filters.private, group=-1)
async def update_msgs(client, message):
    if message.from_user:
        user_id = message.from_user.id
        cr.execute("INSERT OR IGNORE INTO users (user_id, msgs) VALUES (?, 0)", (user_id,))
        cr.execute("UPDATE users SET msgs = msgs + 1 WHERE user_id = ?", (user_id,))
        db.commit()

@Client.on_message(filters.regex("^(ايدي|ا|id|ID)$"))
async def get_id_with_db(client, message):
    target = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    user_id = target.id
    
    # جلب عدد الرسائل من القاعدة
    cr.execute("SELECT msgs FROM users WHERE user_id = ?", (user_id,))
    res = cr.fetchone()
    msgs_count = res[0] if res else 0

    if user_id == Config.OWNER_ID:
        rank = "👑 مطور السورس"
    else:
        rank = "👤 عضو"

    text = (
        f"💎 **بياناتك من القاعدة :**\n"
        f"━━━━━━━━━━━━━━\n"
        f"👤 **الاسم :** {target.first_name}\n"
        f"🆔 **الايدي :** \`{user_id}\`\n"
        f"🎖 **الرتبة :** {rank}\n"
        f"💬 **رسائلك :** {msgs_count}\n"
        f"━━━━━━━━━━━━━━"
    )

    try:
        photos = [p async for p in client.get_chat_photos(user_id, limit=1)]
        if photos:
            await message.reply_photo(photos[0].file_id, caption=text)
        else:
            await message.reply_text(text)
    except:
        await message.reply_text(text)

@Client.on_message(filters.regex("^تصفير الرسائل$") & filters.user(Config.OWNER_ID))
async def reset_msgs(client, message):
    cr.execute("UPDATE users SET msgs = 0")
    db.commit()
    await message.reply("✅ تم تصفير جميع الرسائل في القاعدة.")
EOF
