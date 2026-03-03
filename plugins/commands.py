from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") | filters.regex("^الاوامر$"))
async def crystal_menu(client, message):
    # هنا تقدر تغير الكلام براحتك (لمسات أسامة)
    text = (
        f"🙋‍♂️ **أهلاً بك في سورس كريستال المتطور**\n"
        f"👤 **المطور: أسامة (@U_K44)**\n"
        f"━━━━━━━━━━━━━━\n"
        f"🛠 **استخدم الأزرار بالأسفل للتحكم:**"
    )
    
    # تقسيم الأزرار (ستايل العمدة)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛠 الحماية", callback_data="h_prot"), InlineKeyboardButton("👮‍♂️ الإدارة", callback_data="h_admin")],
        [InlineKeyboardButton("🎭 التسلية", callback_data="h_fun"), InlineKeyboardButton("💰 البنك", callback_data="h_bank")],
        [InlineKeyboardButton("💎 قناة السورس", url="https://t.me/Crystal_Source")]
    ])
    
    await message.reply_text(text, reply_markup=keyboard)
