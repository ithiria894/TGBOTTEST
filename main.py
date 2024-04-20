from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import constants
import controller
from telegram import Bot


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("歡迎加入蟹家軍! 請輸入 Bitget UID 加入vip群.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("欢迎使用！请使用 /start 命令开始对话。")

def get_group_invite_link(bot_token, group_id):
    try:
        bot = Bot(token=bot_token)
        invite_link = bot.export_chat_invite_link(chat_id=group_id)
        return invite_link
    except Exception as e:
        print("Error occurred while getting group invite link:", e)
        return None
    

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'USER ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'private':
        uid = text
        print(uid)
        # if uid == '123':  
        if await controller.is_valid_uid(uid):
            bot_token = constants.TOKEN
            group_id = constants.VIP_GROUP_ID
            invite_link = await get_group_invite_link(bot_token, group_id)
            if invite_link:
                await update.message.reply_text(f"Here is the group invite link: {invite_link}")
            else:
                await update.message.reply_text("Failed to get group invite link. Please try again later.")
        else:
            await update.message.reply_text("這個 UID 不對，請輸入正確的 UID 。")


async def remind_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("欢迎使用！请使用 /start 命令开始对话。")

if __name__ == '__main__':
    app = Application.builder().token(constants.TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
                    
    app.run_polling(poll_interval=3)
