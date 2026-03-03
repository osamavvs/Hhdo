cat <<EOF > ~/Hhdo/plugins/responses.py
from pyrogram import Client, filters

@Client.on_message(filters.regex("^سورس$") & filters.group)
async def source_reply(client, message):
    await message.reply("💎 **سورس كرستال يعمل بنجاح**\n✨ المطور: @OOO2OO")

@Client.on_message(filters.regex("^(شلونك|كيفك)$"))
async def health_reply(client, message):
    await message.reply("بخير دامك بخير يا عسل ✨")
EOF
