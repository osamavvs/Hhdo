from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.regex("^(سورس|السورس|يا سورس)$"))
async def source_info(client, message):
    source_text = (
        f"🙋‍♂️ **أهـلاً بـك عـزيـزي فـي مـعـلـومـات الـسـورس**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"💎 **اسـم الـسـورس : كـرسـتـال ( v1.0 )**\n"
        f"👤 **الـمـطـور : أسـامـة الـعـمـده @U_K44**\n"
        f"⚙️ **الـلـغـة : بـايـثـون ( Pyrogram )**\n"
        f"⚡ **الـحـالـة : يـعـمـل بـكـفـاءة عـالـيـة**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"• تـابـع جـديـد الـتـحـديـثات عـبـر الـقـنـاة ↓"
    )
    
    photo_url = "https://telegra.ph/file/0c62e557b470007883d6a.jpg" 
    
    await message.reply_photo(
        photo=photo_url,
        caption=source_text,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("👨‍💻 الـمـطـور", url="https://t.me/U_K44"),
                InlineKeyboardButton("📢 قـنـاة الـسـورس", url="https://t.me/BBABB9")
            ],
            [
                InlineKeyboardButton("➕ أضـف الـبـوت لـمـجـمـوعـتـك", url=f"https://t.me/{client.me.username}?startgroup=true")
            ]
        ])
    )
