from pyrogram import Client, filters
import random

# مصفوفة الردود على كلمة "اسامه" أو "أسامة"
@Client.on_message(filters.regex("^(اسامه|أسامة|المطور)$"))
async def dev_response(client, message):
    responses = [
        "👑 **تـاج راسـي ومـطـوري الـغـالي أسـامـة**",
        "💎 **لـبـيـه يـا ريـحـة الـهـيـبـة ( أسـامـة الـعـمـده )**",
        "✨ **الـمـطـور أسـامـة @U_K44 هـو الأسـاس**",
        "🙋‍♂️ **نـاديت عـلى عـمـك ومـطـور الـسـورس؟**"
    ]
    await message.reply_text(random.choice(responses))

# مصفوفة الردود على كلمة "البوت" أو "يا بوت"
@Client.on_message(filters.regex("^(بوت|البوت|يا بوت)$"))
async def bot_response(client, message):
    responses = [
        "💎 **اسـمـي كـرسـتـال يـا روحـي، ومـطـوري أسـامـة**",
        "🙋‍♂️ **آمـر يـا بـعـد قـلـبـي، بـوت كـرسـتـال بـخـدمـتـك**",
        "✨ **سـورس كـرسـتـال الـفـخـم يـلـبـي نـداءك**",
        "🛡 **بـوت الـحـمـايـة جـاهـز لـلـتـنـفـيذ**"
    ]
    await message.reply_text(random.choice(responses))

# ردود عامة (السلام عليكم، هلو)
@Client.on_message(filters.regex("^(السلام عليكم|سلام)$"))
async def salam_response(client, message):
    await message.reply_text(
        f"🙋‍♂️ **وعـلـيـكـم الـسـلام يـا {message.from_user.mention}**\n"
        "✨ **نـورت سـورس كـرسـتـال الـخـرافـي**"
    )

@Client.on_message(filters.regex("^(هلو|هلا)$"))
async def hello_response(client, message):
    await message.reply_text(f"💎 **هـلا بـك يـا بـعـد روح كـرسـتـال، نـورتـنا**")

# رد مضحك إذا أحد غلط على البوت
@Client.on_message(filters.regex("^(حمار|كلب|غبي)$"))
async def abuse_response(client, message):
    await message.reply_text("❌ **عـيـب يـا طـيـب، أنـا بـوت مـحـتـرم ومـطـوري أسـامـة يـربـيـك**")
