from pyrogram import Client, filters
from config import Config
import os

# ملفات تخزين البيانات (قاعدة بيانات بسيطة)
USERS_FILE = "users.txt"
GROUPS_FILE = "groups.txt"

def add_user(user_id):
    users = open(USERS_FILE, "a+").read().split()
    if str(user_id) not in users:
        with open(USERS_FILE, "a") as f:
            f.write(f"{user_id}\n")

def add_group(chat_id):
    groups = open(GROUPS_FILE, "a+").read().split()
    if str(chat_id) not in groups:
        with open(GROUPS_FILE, "a") as f:
            f.write(f"{chat_id}\n")

# تسجيل المستخدمين والمجموعات تلقائياً
@Client.on_message(filters.all, group=-1)
async def auto_save(client, message):
    if message.chat.type == "private":
        add_user(message.from_user.id)
    else:
        add_group(message.chat.id)

# --- لوحة التحكم الضخمة ---

@Client.on_message(filters.regex("^(الاحصائيات|الاحصاء)$") & filters.user(Config.OWNER_ID))
async def stats(client, message):
    u_count = len(open(USERS_FILE, "a+").read().split())
    g_count = len(open(GROUPS_FILE, "a+").read().split())
    
    await message.reply_text(
        f"📊 **إحصائيات سورس كرستال:**\n\n"
        f"👤 عدد المستخدمين: `{u_count}`\n"
        f"👥 عدد المجموعات: `{g_count}`\n\n"
        f"✨ الحالة: متصل (Online)"
    )

@Client.on_message(filters.regex("^(لوحة التحكم|التحكم)$") & filters.user(Config.OWNER_ID))
async def admin_panel(client, message):
    await message.reply_text(
        "💎 **أهلاً بك في لوحة تحكم كرستال الضخمة**\n"
        "استخدم الأوامر التالية للتحكم:\n\n"
        "1️⃣ `الاحصائيات` - لعرض الأرقام\n"
        "2️⃣ `اذاعة` - (بالرد على رسالة) للنشر للكل\n"
        "3️⃣ `توجيه` - (بالرد على رسالة) توجيه للكل\n"
        "4️⃣ `نسخة احتياطية` - لجلب ملفات السورس\n"
        "5️⃣ `تحديث` - لإعادة تشغيل البوت"
    )

@Client.on_message(filters.regex("^اذاعة$") & filters.reply & filters.user(Config.OWNER_ID))
async def broadcast(client, message):
    users = open(USERS_FILE, "r").read().split()
    msg = message.reply_to_message
    count = 0
    wait = await message.reply_text("⏳ جاري الإذاعة... يرجى الانتظار")
    
    for user in users:
        try:
            await msg.copy(int(user))
            count += 1
        except:
            pass
    
    await wait.edit(f"✅ تم الإذاعة بنجاح لـ `{count}` مستخدم.")

@Client.on_message(filters.regex("^نسخة احتياطية$") & filters.user(Config.OWNER_ID))
async def backup(client, message):
    await message.reply_document("main.py", caption="📄 نسخة احتياطية لملف التشغيل")
    await message.reply_document(USERS_FILE, caption="👤 نسخة لقاعدة المستخدمين")
