from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# قائمة الأوامر الرئيسية (نفس التصميم السابق)
@Client.on_message(filters.command("help") | filters.regex("^الاوامر$"))
async def help_menu(client, message):
    text = (
        "** CRYSTAL • **\n\n"
        "**الاوامر**\n"
        "**• ⦙ اوامـر الـبوت الـرئيسيـة**\n"
        "**━━━━━━━━━━━━━**\n"
        "**• ⦙ اختـر ماتريـد عرضـه مـن القائمـه :**\n\n"
        "**• ⦙ [قناة السورس والتحديثات](https://t.me/BBABB9)**\n"
        "**━━━━━━━━━━━━━**"
    )
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("م 2 اوامر الادمنيه", callback_data="h_admin"), InlineKeyboardButton("م 1 اوامر الحماية", callback_data="h_protect")],
        [InlineKeyboardButton("م 4 اوامر المنشئين", callback_data="h_creator"), InlineKeyboardButton("م 3 اوامر المدراء", callback_data="h_manager")],
        [InlineKeyboardButton("م 6 اوامر التحشيش", callback_data="h_fun"), InlineKeyboardButton("م 5 اوامر المالكين", callback_data="h_owners")],
        [InlineKeyboardButton("م 8 اوامر البنك", callback_data="h_bank"), InlineKeyboardButton("م 7 اوامر التسليه", callback_data="h_games")],
        [InlineKeyboardButton("م المطور", callback_data="h_source"), InlineKeyboardButton("م 9 اوامر التنظيف", callback_data="h_clean")],
        [InlineKeyboardButton("الالعاب", callback_data="h_all_games")],
        [InlineKeyboardButton("التفعيل / التعطيل", callback_data="h_enable"), InlineKeyboardButton("القفل / الفتح", callback_data="h_lock")],
        [InlineKeyboardButton("✨ MERO SOURCE ™", url="https://t.me/BBABB9")]
    ])
    await message.reply_text(text, reply_markup=buttons, disable_web_page_preview=True)

# --- قسم أوامر الحماية (م 1) كما في الصورة الثانية ---
@Client.on_callback_query(filters.regex("h_protect"))
async def protect_callback(client, query: CallbackQuery):
    protect_text = (
        "** CRYSTAL • **\n\n"
        "**الاوامر**\n"
        "**• ⦙ اوامـر الحمايه كالاتي ...**\n"
        "**━━━━━━━━━━━━━**\n"
        "**• ⦙ قفل ، فتح ← الامر**\n"
        "**• ⦙ تستطيع قفل حمايه كما يلي ...**\n"
        "**• ⦙ ← { بالتقييد ، بالطرد ، بالكتم }**\n"
        "**━━━━━━━━━━━━━**\n"
        "**• ⦙ الكل ~ الدخول**\n"
        "**• ⦙ الروابط ~ المعرف**\n"
        "**• ⦙ التاك ~ الشارحه**\n"
        "**• ⦙ التعديل ~ تعديل الميديا**\n"
        "**• ⦙ المتحركه ~ الملفات**\n"
        "**• ⦙ الصور ~ الفيديو**\n"
        "**━━━━━━━━━━━━━**\n"
        "**• ⦙ الماركدوان ~ البوتات**\n"
        "**• ⦙ التكرار ~ الكلايش**\n"
        "**• ⦙ السيلفي ~ الملصقات**\n"
        "**• ⦙ الاونلاين ~ الدردشه**\n"
        "**• ⦙ الهمسه**\n"
        "**━━━━━━━━━━━━━**\n"
        "**• ⦙ التوجيه ~ الاغاني**\n"
        "**• ⦙ الصوت ~ الجهات**\n"
        "**• ⦙ الاشعارات ~ التثبيت**\n"
        "**• ⦙ الوسائط ~ التفليش**\n"
        "**• ⦙ وسائط المميزين**\n"
        "**• ⦙ الفشار ~ ارسال القناة**\n"
        "**• ⦙ القنوات ~ الموقع**\n"
        "**• ⦙ الإنكليزيه ~ الفارسيه**\n"
        "**• ⦙ الكفر ~ الاباحي**\n"
        "**• ⦙ التشويش ~ الملصقات المميزه**\n"
        "**━━━━━━━━━━━━━**"
    )
    
    back_button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ رجوع", callback_data="h_back")]])
    await query.edit_message_text(protect_text, reply_markup=back_button)

# معالج زر الرجوع
@Client.on_callback_query(filters.regex("h_back"))
async def back_to_main(client, query: CallbackQuery):
    # إعادة استدعاء القائمة الرئيسية
    await help_menu(client, query.message)
    await query.message.delete()
