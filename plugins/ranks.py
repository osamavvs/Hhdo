cat <<EOF > ~/Hhdo/plugins/ranks.py
from pyrogram import Client, filters
from config import Config
from db_handler import db, cr

@Client.on_message(filters.group | filters.private, group=-1)
async def counter(client, message):
    if message.from_user:
        user_id = message.from_user.id
        cr.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
        cr.execute("UPDATE users SET msgs = msgs + 1 WHERE user_id = ?", (user_id,))
        db.commit()

@Client.on_message(filters.regex("^(ايدي|ا|id)$"))
async def id_handler(client, message):
    target = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    cr.execute("SELECT msgs FROM users WHERE user_id = ?", (target.id,))
    res = cr.fetchone()
    msgs = res[0] if res else 0
    
    rank = "👑 مطور السورس" if target.id == Config.OWNER_ID else "👤 عضو"
    
    caption = (
        f"💎 **سورس كرستال**\n"
        f"━━━━━━━━━━━━━━\n"
        f"👤 **الاسم:** {target.first_name}\n"
        f"🆔 **الايدي:** \`{target.id}\`\n"
        f"🎖 **الرتبة:** {rank}\n"
        f"💬 **رسائلك:** {msgs}\n"
        f"━━━━━━━━━━━━━━"
    )
    
    try:
        photos = [p async for p in client.get_chat_photos(target.id, limit=1)]
        if photos:
            await message.reply_photo(photos[0].file_id, caption=caption)
        else:
            await message.reply_text(caption)
    except:
        await message.reply_text(caption)
EOF
