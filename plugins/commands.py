from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import Config

# --- واجهة الأوامر الرئيسية (ستايل العمدة) ---
@Client.on_message(filters.command("start") | filters.regex("^الاوامر$"))
async def omda_menu(client, message):
    text = (
        f"‏  ‌‌‏ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ\n"
        f"🙋‍♂️ **أهلاً بك عزيزي في أوامر بوت كريستال**\n"
        f"👤 **المطور الأساسي : [أسامة](t.me/U_K44)**\n"
        f"━━━━━━━━━━━━━━\n"
        f"⚙️ **قائمة التحكم الرئيسية للبوت أدناه :**\n"
        f"━━━━━━━━━━━━━━"
    )
    
    # توزيع الأزرار بنفس نمط سورس العمدة
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🛠 أوامر الحماية", callback_data="h_prot"),
            InlineKeyboardButton("👮‍♂️ أوامر الأدمنية", callback_data="h_admin")
        ],
        [
            InlineKeyboardButton("📋 أوامر المدير", callback_data="h_mgr"),
            InlineKeyboardButton("💎 أوامر المنشئ", callback_data="h_creator")
        ],
        [
            InlineKeyboardButton("👑 أوامر المالك", callback_data="h_owner"),
            InlineKeyboardButton("🔥 أوامر المطور", callback_data="h_sudo")
        ],
        [
            InlineKeyboardButton("💰 أوامر البنك", callback_data="h_bank"),
            InlineKeyboardButton("🎭 أوامر التسلية", callback_data="h_fun")
        ],
        [
            InlineKeyboardButton("🧹 أوامر التنظيف", callback_data="h_clean"),
            InlineKeyboardButton("🎮 ألعاب كريستال", callback_data="h_games")
        ],
        [
            InlineKeyboardButton("🔐 قفل / فتح", callback_data="h_locks"),
            InlineKeyboardButton("🔔 تفعيل / تعطيل", callback_data="h_toggle")
        ],
        [
            InlineKeyboardButton("💎 قناة السورس 💎", url="https://t.me/Crystal_Source")
        ]
    ])
    
    await message.reply_text(text, reply_markup=keyboard, disable_web_page_preview=True)

# --- معالج الأزرار (Callbacks) ---
@Client.on_callback_query()
async def on_click(client, callback: CallbackQuery):
    data = callback.data
    
    if data == "h_prot":
        await callback.edit_message_text(
            "🛠 **أوامر الحماية والتحكم:**\n━━━━━━━━━━━━━━\n"
            "● قفل/فتح الروابط\n"
            "● قفل/فتح التوجيه\n"
            "● قفل/فتح المعرفات\n"
            "● قفل/فتح التكرار\n━━━━━━━━━━━━━━",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع 🔙", callback_data="main_omda")]])
        )
    
    elif data == "main_omda":
        # العودة للقائمة الرئيسية
        await callback.edit_message_text(
            f"🙋‍♂️ **أهلاً بك في أوامر سورس كريستال**\n━━━━━━━━━━━━━━",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🛠 أوامر الحماية", callback_data="h_prot"), InlineKeyboardButton("👮‍♂️ أوامر الأدمنية", callback_data="h_admin")],
                [InlineKeyboardButton("💎 أوامر المطور", callback_data="h_sudo")],
                [InlineKeyboardButton("🔙 العودة للقائمة", callback_data="main_omda")]
            ])
        )
