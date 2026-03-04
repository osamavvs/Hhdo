from os import getenv
from dotenv import load_dotenv

# إذا كنت تستخدم ملف .env قم بتفعيل هذا السطر
# load_dotenv()

# --- إعدادات الحساب والبوت ---
# استخرجها من my.telegram.org
API_ID = int(getenv("API_ID", "24752047")) 
API_HASH = getenv("API_HASH", "5b8a468627791bdd36a8c361913b0b72")

# استخرجه من @BotFather
BOT_TOKEN = getenv("BOT_TOKEN", "8787399797:AAHWPuu_aryslF5sSAiDEBoSWY9AtpaUGdo")

# جلسة الحساب المساعد (String Session)
STRING_SESSION = getenv("STRING_SESSION", "AgF5r68AEOXpzc7wK6StVu_G53EF7j1XDr4bhnrEQYPo8rbjHUHZ_UEXXBZuZtJ1HFQ9xxYWtUm6pDXrG6GTI3UGHZOHuQVXlFCQX69XmrAeZF-IXxXjemhy75B9C7TUeWMony9lKmSYQNY33j28ytqegvlAxe5MAWE_F42SP0r81ARIuPUzSUROxGyqr_bib_EOgIqouUmD_CZMPsBeiaUPeoIipcIxRLyw9i4p3-dhX3J0B-87XG2KoCxv4FAI3DAe9Yl7SEjPHAo9IRcBvxEI_1HtQDaFWkitb_-JZgfkkcPxa_xObU8NYmHXeT-1nJ6EmEwxeP1JRqcCCW1TsyJsHZIDQwAAAAHb4UXaAA")

# --- إعدادات المطورين (SUDO) ---
# ضع آيديك هنا لكي يستجيب البوت لأوامرك
# يمكنك الحصول على الآيدي بإرسال /id لبوت @userinfobot
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8074717568").split())) 

# آيدي المالك الأساسي
OWNER_ID = int(getenv("OWNER_ID", "8074717568"))

# --- إعدادات إضافية ---
# رابط قناة السورس أو الدعم
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BBABB9")
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/your_image.jpg")
