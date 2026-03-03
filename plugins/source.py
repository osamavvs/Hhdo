from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(filters.regex("^(سورس|السورس|يا سورس)$"))
async def source_info(client, message: Message):
    # رابط الصورة (يمكنك استبداله برابط صورتك الخاصة)
    source_photo_url = "https://telegra.ph/file/0230d5d2c0b490f230d5d.jpg"
    
    # نص الرسالة
    text = (
        "💎 ** CRYSTAL SOURCE • **\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "✨ **اقوى سورس حماية وتسلية على التليجرام**\n"
        "👑 **سلطان العمدة يرحب بكم في سورس كرستال**\n\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    
    # الأزرار (المطور والسورس في أزرار)
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("👤 المطور", url="https://t.me/U_K44"),
            InlineKeyboardButton("⚙️ السورس", url="https://t.me/BBABB9")
        ],
        [
            InlineKeyboardButton("➕ أضف البوت لمجموعتك ➕", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")
        ]
    ])
    
    try:
        await message.reply_photo(
            photo=source_photo_url,
            caption=text,
            reply_markup=buttons
        )
    except Exception:
        await message.reply_text(
            text,
            reply_markup=buttons
        )
