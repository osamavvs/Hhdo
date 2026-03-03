cat <<EOF > ~/Hhdo/plugins/replies.py
from pyrogram import Client, filters
from config import Config
import sqlite3

# الاتصال بالقاعدة وتجهيز جدول الردود
db = sqlite3.connect("crystal.db", check_same_thread=False)
cr = db.cursor()

@Client.on_message(filters.regex("^اضف رد (.*)$") & filters.user(Config.OWNER_ID))
async def save_reply(client, message):
    word = message.matches[0].group(1)
    if not message.reply_to_message:
        return await message.reply(f"⚠️ **رد على (نص، صورة، ملصق) عشان أحفظه للكلمة: [{word}]**")
    
    rep = message.reply_to_message
    r_type = "text"
    file_id = rep.text # افتراضي للنص
    
    # تحديد النوع و ID الملف
    if rep.photo: r_type, file_id = "photo", rep.photo.file_id
    elif rep.sticker: r_type, file_id = "sticker", rep.sticker.file_id
    elif rep.voice: r_type, file_id = "voice", rep.voice.file_id
    elif rep.video: r_type, file_id = "video", rep.video.file_id
    elif rep.animation: r_type, file_id = "animation", rep.animation.file_id

    cr.execute("INSERT OR REPLACE INTO replys VALUES (?, ?, ?)", (word, file_id, r_type))
    db.commit()
    await message.reply(f"✅ **تم حفظ الرد بنجاح!**\nالكلمة: **{word}**\nالنوع: **{r_type}**")

@Client.on_message(filters.regex("^مسح رد (.*)$") & filters.user(Config.OWNER_ID))
async def del_reply(client, message):
    word = message.matches[0].group(1)
    cr.execute("DELETE FROM replys WHERE word = ?", (word,))
    db.commit()
    await message.reply(f"🗑 **تم حذف الرد [{word}]**")

# --- محرك الردود التلقائي ---
@Client.on_message(filters.text & ~filters.private, group=5)
async def auto_reply(client, message):
    cr.execute("SELECT reply_id, type FROM replys WHERE word = ?", (message.text,))
    res = cr.fetchone()
    if res:
        f_id, r_type = res[0], res[1]
        try:
            if r_type == "text": await message.reply(f_id)
            elif r_type == "photo": await message.reply_photo(f_id)
            elif r_type == "sticker": await message.reply_sticker(f_id)
            elif r_type == "voice": await message.reply_voice(f_id)
            elif r_type == "video": await message.reply_video(f_id)
            elif r_type == "animation": await message.reply_animation(f_id)
        except Exception as e:
            print(f"Error in reply: {e}")
EOF
