cat <<EOF > ~/Hhdo/plugins/commands.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

@Client.on_message(filters.regex("^(الاوامر)$"))
async def commands_list(client, message):
    # نص الترحيب المزخرف بستايل سورس العمدة
    caption = (
        f"🙋‍♂️ **أهلاً بك عزيزي في أوامر البوت**\n"
        f"👤 **المطور الأساسي : [أسامة](t.me/U_K44)**\n"
        f"━━━━━━━━━━━━━━\n"
        f"⚙️ **قائمة التحكم الرئيسية للبوت أدناه :**\n"
        f"━━━━━━━━━━━━━━"
    )
    
    # ترتيب الأزرار بنفس نمط سورس العمدة (كل اثنين بجانب بعض)
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🛠 أوامر الحماية", callback_data="help_protect"),
            InlineKeyboardButton("👮‍♂️ أوامر الأدمنية", callback_data="help_admin")
        ],
        [
            InlineKeyboardButton("📋 أوامر المدير", callback_data="help_manager"),
            InlineKeyboardButton("💎 أوامر المنشئ", callback_data="help_creator")
        ],
        [
            InlineKeyboardButton("👑 أوامر المالك", callback_data="help_owner"),
            InlineKeyboardButton("🔥 أوامر المطور", callback_data="help_sudo")
        ],
        [
            InlineKeyboardButton("💰 أوامر البنك", callback_data="help_bank"),
            InlineKeyboardButton("🎭 أوامر التسلية", callback_data="help_fun")
        ],
        [
            InlineKeyboardButton("🧹 أوامر التنظيف", callback_data="help_clean"),
            InlineKeyboardButton("🎮 ألعاب كريستال", callback_data="help_games")
        ],
        [
            InlineKeyboardButton("🔐 قفل / فتح", callback_data="help_locks"),
            InlineKeyboardButton("🔔 تفعيل / تعطيل", callback_data="help_toggle")
        ],
        [
            InlineKeyboardButton("💎 قناة السورس 💎", url="https://t.me/Crystal_Source")
        ]
    ])
    
    await message.reply_text(caption, reply_markup=keyboard, disable_web_page_preview=True)

EOF
