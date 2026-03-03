cat <<EOF > ~/Hhdo/plugins/sudo.py
from pyrogram import Client, filters
from config import Config
import os
import sys
import sqlite3

def get_db():
    db = sqlite3.connect("crystal.db", check_same_thread=False)
    return db, db.cursor()

@Client.on_message(filters.regex("^(تحديث|ت)$") & filters.user(Config.OWNER_ID))
async def restart_bot(client, message):
    await message.reply("🚀 **جاري التحديث وإعادة التشغيل الفوري...**")
    # هذه الطريقة تستبدل النسخة القديمة بالجديدة برمجياً بدون توقف
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.regex("^اضف رد (.*)$") & filters.user(Config.OWNER_ID))
async def save_reply(client, message):
    word = message.matches[0].group(1).strip()
    if not message.reply_to_message:
        return await message.reply("⚠️ **رد على (نص، صورة، ملصق) لإضافته.**")
    
    db, cr = get_db()
    rep = message.reply_to_message
    r_type = "text"
    file_id = rep.text
    
    if rep.photo: r_type, file_id = "photo", rep.photo.file_id
    elif rep.sticker: r_type, file_id = "sticker", rep.sticker.file_id
    elif rep.voice: r_type, file_id = "voice", rep.voice.file_id
    elif rep.video: r_type, file_id = "video", rep.video.file_id
    elif rep.animation: r_type, file_id = "animation", rep.animation.file_id

    cr.execute("INSERT OR REPLACE INTO replys VALUES (?, ?, ?)", (word, file_id, r_type))
    db.commit()
    await message.reply(f"✅ **تم حفظ الرد للكلمة: {word}**")

@Client.on_message(filters.text & ~filters.private, group=1)
async def auto_reply(client, message):
    db, cr = get_db()
    word = message.text.strip()
    cr.execute("SELECT reply_id, type FROM replys WHERE word = ?", (word,))
    res = cr.fetchone()
    if res:
        f_id, r_type = res[0], res[1]
        if r_type == "text": await message.reply(f_id)
        elif r_type == "photo": await message.reply_photo(f_id)
        elif r_type == "sticker": await message.reply_sticker(f_id)
        elif r_type == "voice": await message.reply_voice(f_id)
        elif r_type == "video": await message.reply_video(f_id)
        elif r_type == "animation": await message.reply_animation(f_id)
EOF
