from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import Config

@Client.on_message(filters.private & filters.command("start"))
async def start_private(client, message: Message):
    # رابط صورة الترحيب (يمكنك استبدالها برابط صورتك)
    start_photo = "https://telegra.ph/file/0230d5d2c0b490f230d5d.jpg"
    
    # نص الترحيب الفخم
    text = (
        f"🙋‍♂️ **أهـلاً بـك عـزيـزي {message.from_user.mention}**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"✨ **أنـا بـوت حـمـايـة وتـسـلـيـة الـمـجـموعات**\n"
        f"💎 **سـورس كـرسـتـال يـقـدم لـك أقـوى الـمـمـيزات**\n\n"
        f"📩 **يـمـكـنـك مراسـلة الـمطور مـباشـرة عـبـر الـبوت**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👑 **الـمـطـور : أسـامـة @U_K44**"
    )
    
    # أزرار الخاص
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ أضف البوت لمجموعتك ➕", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")
        ],
        [
            InlineKeyboardButton("⚙️ أوامر البوت", callback_data="h_back"), # يفتح قائمة الأوامر
            InlineKeyboardButton("💎 قناة السورس", url="https://t.me/BBABB9")
        ],
        [
            InlineKeyboardButton("👤 مطور السورس", url="https://t.me/U_K44")
        ]
    ])
    
    # إرسال الترحيب
    try:
        await message.reply_photo(
            photo=start_photo,
            caption=text,
            reply_markup=buttons
        )
    except:
        await message.reply_text(
            text,
            reply_markup=buttons
        )
    
    # تنبيهك أنت (أسامة) بدخول مستخدم جديد
    if message.from_user.id != Config.OWNER_ID:
        try:
            await client.send_message(
                Config.OWNER_ID,
                f"👤 **مـسـتـخـدم جـديـد دخـل لـلـخـاص :**\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"🙋‍♂️ **الاسـم:** {message.from_user.mention}\n"
                f"🆔 **الايدي:** `{message.from_user.id}`\n"
                f"✨ **يـوزر:** @{message.from_user.username if message.from_user.username else 'لا يوجد'}"
            )
        except:
            pass
