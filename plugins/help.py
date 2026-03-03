from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("help") | filters.regex("^الاوامر$"))
async def help_menu(client, message):
    # الكليشة العلوية كما في الصورة
    text = (
        "** CRYSTAL • **\n\n"
        "**الاوامر**\n"
        "**• ⦙ اوامـر الـبوت الـرئيسيـة**\n"
        "**━━━━━━━━━━━━━**\n"
        "**• ⦙ اختـر ماتريـد عرضـه مـن القائمـه :**\n\n"
        "**• ⦙ [قناة السورس والتحديثات](https://t.me/BBABB9)**\n"
        "**━━━━━━━━━━━━━**"
    )
    
    # توزيع الأزرار صفين صفين مثل الصورة بالضبط
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("م 2 اوامر الادمنيه", callback_data="h_admin"),
            InlineKeyboardButton("م 1 اوامر الحماية", callback_data="h_protect")
        ],
        [
            InlineKeyboardButton("م 4 اوامر المنشئين", callback_data="h_creator"),
            InlineKeyboardButton("م 3 اوامر المدراء", callback_data="h_manager")
        ],
        [
            InlineKeyboardButton("م 6 اوامر التحشيش", callback_data="h_fun"),
            InlineKeyboardButton("م 5 اوامر المالكين", callback_data="h_owners")
        ],
        [
            InlineKeyboardButton("م 8 اوامر البنك", callback_data="h_bank"),
            InlineKeyboardButton("م 7 اوامر التسليه", callback_data="h_games")
        ],
        [
            InlineKeyboardButton("م المطور", callback_data="h_source"),
            InlineKeyboardButton("م 9 اوامر التنظيف", callback_data="h_clean")
        ],
        [
            InlineKeyboardButton("الالعاب", callback_data="h_all_games")
        ],
        [
            InlineKeyboardButton("التفعيل / التعطيل", callback_data="h_enable"),
            InlineKeyboardButton("القفل / الفتح", callback_data="h_lock")
        ],
        [
            InlineKeyboardButton("✨ MERO SOURCE ™", url="https://t.me/BBABB9")
        ]
    ])
    
    await message.reply_text(
        text, 
        reply_markup=buttons, 
        disable_web_page_preview=True
    )
