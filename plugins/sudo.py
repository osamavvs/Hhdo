cat <<EOF > ~/Hhdo/plugins/sudo.py
from pyrogram import Client, filters
from config import Config
from db_handler import db, cr, is_sudo

@Client.on_message(filters.regex("^(رفع مطور)$") & filters.user(Config.OWNER_ID))
async def add_sudo(client, message):
    if not message.reply_to_message:
        return await message.reply("⚡️ عذراً، يجب الرد على المستخدم لرفعه مطور.")
    
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    
    cr.execute("INSERT OR IGNORE INTO sudos (user_id) VALUES (?)", (user_id,))
    db.commit()
    await message.reply(f"👤 المستخدم: **{user_name}**\n✅ تم رفعه مطور في السورس بنجاح.")

@Client.on_message(filters.regex("^(تنزيل مطور)$") & filters.user(Config.OWNER_ID))
async def rem_sudo(client, message):
    if not message.reply_to_message:
        return await message.reply("⚡️ عذراً، يجب الرد على المستخدم لتنزيله.")
    
    user_id = message.reply_to_message.from_user.id
    cr.execute("DELETE FROM sudos WHERE user_id = ?", (user_id,))
    db.commit()
    await message.reply("✅ تم تنزيل المستخدم من المطورين.")

@Client.on_message(filters.regex("^(المطورين)$") & filters.user(Config.OWNER_ID))
async def list_sudos(client, message):
    cr.execute("SELECT user_id FROM sudos")
    rows = cr.fetchall()
    if not rows:
        return await message.reply("⚠️ لا يوجد مطورين مرفوعين حالياً.")
    
    text = "💎 **قائمة مطورين كرستال :**\n━━━━━━━━━━━━━━\n"
    for i, row in enumerate(rows, 1):
        text += f"{i} - \`{row[0]}\`\n"
    await message.reply(text)
EOF
