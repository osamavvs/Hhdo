from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("help") | filters.regex("^الاوامر$"))
async def help_menu(client, message):
    # كليشة العمدة الفخمة
    text = (
        "👑 ** CRYSTAL SOURCE • **\n\n"
        "🙋‍♂️ **أهلاً بك عزيزي في أوامر السورس**\n"
        "✨ **مطور السورس : أسامة @U_K44**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⚙️ **قائمة التحكم الرئيسية ↓**\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    
    # توزيع الأزرار (نفس نمط العمدة: صفوف ثنائية متناسقة)
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("م 1 اوامر الحمايه", callback_data="h_protect"),
            InlineKeyboardButton("م 2 اوامر الادمنيه", callback_data="h_admin")
        ],
        [
            InlineKeyboardButton("م 3 اوامر المدراء", callback_data="h_manager"),
            InlineKeyboardButton("م 4 اوامر المنشئين", callback_data="h_creator")
        ],
        [
            InlineKeyboardButton("م 5 اوامر المالكين", callback_data="h_owners"),
            InlineKeyboardButton("م 6 اوامر التحشيش", callback_data="h_fun")
        ],
        [
            InlineKeyboardButton("م 7 اوامر التسليه", callback_data="h_games"),
            InlineKeyboardButton("م 8 اوامر البنك", callback_data="h_bank")
        ],
        [
            InlineKeyboardButton("م 9 اوامر التنظيف", callback_data="h_clean"),
            InlineKeyboardButton("م المطور", callback_data="h_source")
        ],
        [
            InlineKeyboardButton("🎮 الـعـاب كـرسـتـال 🎮", callback_data="h_all_games")
        ],
        [
            InlineKeyboardButton("قفل / فتح", callback_data="h_lock"),
            InlineKeyboardButton("تفعيل / تعطيل", callback_data="h_enable")
        ],
        [
            InlineKeyboardButton("💎 قـنـاة الـسـورس 💎", url="https://t.me/BBABB9")
        ]
    ])
    
    await message.reply_text(
        text, 
        reply_markup=buttons, 
        disable_web_page_preview=True
    )
