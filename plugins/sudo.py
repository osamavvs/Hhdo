cat <<EOF > ~/Hhdo/plugins/sudo.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
import sqlite3
import json
import os

# الاتصال بالقاعدة وتجهيز جداول الردود
db = sqlite3.connect("crystal.db", check_same_thread=False)
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS replys (word TEXT PRIMARY KEY, reply_id TEXT, type TEXT)")
db.commit()

# --- [ نظام الردود الذكي ] ---

@Client.on_message(filters.regex("^اضف رد$") & filters.user(Config.OWNER_ID))
async def add_reply_step(client, message):
    await message.reply("⚙️ **ارسل الآن الكلمة التي تريد إضافتها..**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("إلغاء ❌", callback_data="cancel")]]))
    # هنا نجعل البوت ينتظر الكلمة (سأبسطها لك لتكون مباشرة)

@Client.on_message(filters.regex("^اضف رد (.*)$") & filters.user(Config.OWNER_ID))
async def save_reply(client, message):
    word = message.matches[0].group(1)
    if not message.reply_to_message:
        return await message.reply(f"⚠️ **يجب الرد على (نص، صورة، صوت، ملصق) لحفظه كـ رد لـ [{word}]**")
    
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
    await message.reply(f"✅ **تم حفظ الرد بنجاح!**\nالكلمة: {word}\nالنوع: {r_type}")

@Client.on_message(filters.regex("^مسح رد (.*)$") & filters.user(Config.OWNER_ID))
async def del_reply(client, message):
    word = message.matches[0].group(1)
    cr.execute("DELETE FROM replys WHERE word = ?", (word,))
    db.commit()
    await message.reply(f"🗑 **تم حذف الرد [{word}] من القاعدة.**")

# --- [ نظام الإذاعة الشامل ] ---

@Client.on_message(filters.regex("^اذاعة$") & filters.user(Config.OWNER_ID) & filters.reply)
async def broadcast(client, message):
    msg = await message.reply("⏳ **جاري الإذاعة للمجموعات...**")
    cr.execute("SELECT user_id FROM users") # افتراضياً نذيع للمستخدمين
    users = cr.fetchall()
    done = 0
    for user in users:
        try:
            await message.reply_to_message.copy(user[0])
            done += 1
        except: continue
    await msg.edit(f"✅ **تمت الإذاعة لـ {done} مستخدم.**")

# --- [ تشغيل الردود تلقائياً ] ---

@Client.on_message(filters.text & filters.group, group=2)
async def auto_reply(client, message):
    cr.execute("SELECT reply_id, type FROM replys WHERE word = ?", (message.text,))
    res = cr.fetchone()
    if res:
        f_id, r_type = res[0], res[1]
        if r_type == "text": await message.reply(f_id)
        elif r_type == "photo": await message.reply_photo(f_id)
        elif r_type == "sticker": await message.reply_sticker(f_id)
        elif r_type == "voice": await message.reply_voice(f_id)
        elif r_type == "video": await message.reply_video(f_id)
        elif r_type == "animation": await message.reply_animation(f_id)

# --- [ تحديث و رست ] ---

@Client.on_message(filters.regex("^(تحديث|رست)$") & filters.user(Config.OWNER_ID))
async def restart_vps(client, message):
    await message.reply("⚙️ **جاري تحديث ملفات السورس وإعادة التشغيل...**")
    os.execl(os.sys.executable, os.sys.executable, *os.sys.argv)
EOF
