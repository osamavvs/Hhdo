from telebot.types import ChatPermissions

def تسجيل(bot):

    @bot.message_handler(commands=['كتم'])
    def كتم(message):
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            bot.restrict_chat_member(
                message.chat.id,
                user_id,
                ChatPermissions(can_send_messages=False)
            )
            bot.reply_to(message, "تم كتم العضو 🔇")

    @bot.message_handler(commands=['الغاء_كتم'])
    def الغاء_كتم(message):
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            bot.restrict_chat_member(
                message.chat.id,
                user_id,
                ChatPermissions(can_send_messages=True)
            )
            bot.reply_to(message, "تم الغاء الكتم ✅")
