import telebot

YOUR_BOT_TOKEN="6454485391:AAGXnoyfYfizDPcHgjDKSQruzSFY-xs02R0"
API_TOKEN = YOUR_BOT_TOKEN

bot = telebot.TeleBot(API_TOKEN)

def get_group_invite_link():
    chat_id = '-1002087737560'
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
def handle_message(message):
    if message.chat.type == 'private':
        uid = message.text
        print(uid)
        if uid == "123":
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

def main():
    bot.polling()

if __name__ == "__main__":
    main()
