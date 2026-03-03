cat <<EOF > ~/Hhdo/plugins/commands.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import Config

# --- الرسالة الرئيسية ---
@Client.on_message(filters.command("start") | filters.regex("^الاوامر$"))
async def start_menu(client, message):
    text = (
        f"‏  ‌‌‏ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ\n"
        f"🙋‍♂️ **مرحباً بك عزيزي {message.from_user.mention}**\n\n"
        f"💎 **أنا بوت ( كريستال ) المتطور لإدارة المجموعات**\n"
        f"🛡 **اختر ما تريد التحكم به من الأزرار أدناه**\n"
        f"━━━━━━━━━━━━━━\n"
        f"👤 **المطور: [أسامة](t.me/U_K44)**\n"
        f"‏  ‌‌‏ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ"
    )
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔐 أوامر القفل", callback_data="help_locks"),
            InlineKeyboardButton("👮‍♂️ أوامر الإدارة", callback_data="help_admin")
        ],
        [
            InlineKeyboardButton("📋 أوامر المدير", callback_data="help_manager"),
            InlineKeyboardButton("🎭 أوامر التسلية", callback_data="help_fun")
        ],
        [
            InlineKeyboardButton("💎 أوامر المطور", callback_data="help_sudo")
        ],
        [
            InlineKeyboardButton("➕ أضف البوت لمجموعتك ➕", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")
        ]
    ])
    
    await message.reply_text(text, reply_markup=keyboard)

# --- معالج الضغط على الأزرار (Callbacks) ---
@Client.on_callback_query()
async def on_click(client, callback: CallbackQuery):
    data = callback.data
    
    if data == "help_locks":
        await callback.edit_message_text(
            "🔐 **قائمة أوامر القفل والفتح:**\n\n"
            "● قفل/فتح الروابط\n"
            "● قفل/فتح الصور\n"
            "● قفل/فتح الفيديو\n"
            "● قفل/فتح التوجيه\n"
            "● قفل/فتح الملفات\n\n"
            "‏  ‌‌‏ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("العودة 🔙", callback_data="back_main")]])
        )

    elif data == "help_admin":
        await callback.edit_message_text(
            "👮‍♂️ **قائمة أوامر الأدمنية:**\n\n"
            "● طرد (بالرد)\n"
            "● كتم (بالرد)\n"
            "● حظر (بالرد)\n"
            "● رفع/تنزيل أدمن\n\n"
            "‏  ‌‌‏ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("العودة 🔙", callback_data="back_main")]])
        )

    elif data == "help_sudo":
        if callback.from_user.id != Config.OWNER_ID:
            return await callback.answer("❌ هذا القسم خاص بالمطور أسامة فقط!", show_alert=True)
        
        await callback.edit_message_text(
            "💎 **أوامر مطور السورس (أسامة):**\n\n"
            "● تحديث (لتحديث ملفات البوت)\n"
            "● اذاعة (لإرسال رسالة لكل المجموعات)\n"
            "● جلب نسخة (لجلب قاعدة البيانات)\n\n"
            "‏  ‌‌‏ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("العودة 🔙", callback_data="back_main")]])
        )

    elif data == "back_main":
        # إعادة القائمة الرئيسية
        await callback.edit_message_text(
            f"‏  ‌‌‏ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ—ـ\n"
            f"🙋‍♂️ **مرحباً بك عزيزي {callback.from_user.mention}**\n\n"
            f"💎 **قائمة أوامر سورس كريستال:**\n"
            f"━━━━━━━━━━━━━━",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔐 أوامر القفل", callback_data="help_locks"), InlineKeyboardButton("👮‍♂️ أوامر الإدارة", callback_data="help_admin")],
                [InlineKeyboardButton("📋 أوامر المدير", callback_data="help_manager"), InlineKeyboardButton("🎭 أوامر التسلية", callback_data="help_fun")],
                [InlineKeyboardButton("💎 أوامر المطور", callback_data="help_sudo")]
            ])
        )
EOF
