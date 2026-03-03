@Client.on_message(filters.group & filters.regex("^(رتبتي|كشف)$"))
async def check_rank(client, message):
    user_id = message.from_user.id
    if user_id == Config.OWNER_ID:
        rank = "👑 مطور السورس أسامة"
    elif user_id in Config.SUDO_USERS:
        rank = "💎 مطور ثانوي"
    else:
        member = await client.get_chat_member(message.chat.id, user_id)
        if member.status.value == "owner": rank = "👑 مالك المجموعة"
        elif member.status.value == "administrator": rank = "🛠 أدمن المجموعة"
        else: rank = "👤 عضو طبيعي"
    
    await message.reply(f"🙋‍♂️ **عزيزي :** {message.from_user.mention}\n✨ **رتبتك هي :** {rank}")
