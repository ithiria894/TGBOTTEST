import telebot
import constants
import controller

bot = telebot.TeleBot(constants.TOKEN)

def get_group_invite_link():
    chat_id = constants.VIP_GROUP_ID
    try:
        invite_link = bot.export_chat_invite_link(chat_id)
        return invite_link
    except telebot.apihelper.ApiException as e:
        print("Telegram API Exception:", e)
    except Exception as e:
        print("Error occurred while getting group invite link:", e)
    return None

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "歡迎加入蟹家軍! 請輸入 Bitget UID 加入vip群.")

@bot.message_handler(func=lambda message: True)
async def handle_message(message):
    if message.chat.type == 'private':
        uid = message.text
        print(uid)
        if await controller.is_valid_uid(uid):
            invite_link = get_group_invite_link()
            if invite_link:
                bot.reply_to(message, f"Here is the group invite link: {invite_link}")
            else:
                bot.reply_to(message, "Failed to get group invite link. Please try again later.")
        else:
            bot.reply_to(message, "這個 UID 不對，請輸入正確的 UID ， 請使用 /start 命令。 （小提示：UID 是 123）")

@bot.message_handler(func=lambda message: message.text == "/start", content_types=['text'])
def remind_start(message):
    bot.reply_to(message, "欢迎使用！请使用 /start 命令开始对话。")

if __name__ == "__main__":
    bot.polling()
