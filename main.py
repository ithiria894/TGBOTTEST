from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, RateLimiter
import constants
import controller

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = InlineKeyboardButton("Start", callback_data="start")
    keyboard = InlineKeyboardMarkup([[button]])
    await update.message.reply_text("""🦀≡≡≡≡≡≡≡≡▷►◈◄◁≡≡≡≡≡≡≡≡🦀
🔝歡迎各位加入🪣比奇堡海之霸VIP🔇
此群主要功能為統計手續費返還名單📝
帶單及訂單分享只是給予忠實粉絲的附加功能
因我個人的策略關係，(槓桿高，盈虧比高)📈
有些訂單接受度較低，在大群發布容易被噴
因此簡單設立一個門檻，避免路人粉瞎操作爆倉
其餘都是沒有任何條件限制
無論妳有沒有入金
甚至沒KYC都是不影響的✅
切記一定要看完至頂留言‼️
內容：
🅰️全宇宙最高60%合約40%現貨手續費減免
🅱️專屬團隊bitget跟單服務
📈VIP群高盈虧比策略分享
🧽交流群加入資格
加入步驟：
1️⃣點擊連結註冊帳號
https://partner.bitget.fit/bg/WedJatBTC
2️⃣輸入UID共10碼
⚠️邀請連結為一次性使用⚠️
⚠️註冊後記得點擊下方加入在退出⚠️
⚠️否則無法再次點擊⚠️
🦀≡≡≡≡≡≡≡≡▷►◈◄◁≡≡≡≡≡≡≡≡🦀""")

def get_group_invite_link(group_id, context: ContextTypes.DEFAULT_TYPE):
    try:
        return context.bot.create_chat_invite_link(chat_id=group_id, member_limit=1)
    except Exception as e:
        print("Error occurred while getting group invite link:", e)
        return
    

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'USER ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'private':
        uid = text
        print(uid)
        # if uid == '123':  
        if await controller.is_valid_uid(uid):
            group_id = constants.VIP_GROUP_ID
            invite_link = await get_group_invite_link(group_id, context)
            if invite_link.invite_link:
                await update.message.reply_text(f"歡迎加入蟹家軍: {invite_link.invite_link}")
            else:
                await update.message.reply_text("邀請連結出錯, 請聯絡蟹老闆後台驗證, 謝謝合作.")
        else:
            await update.message.reply_text("""這個 UID 不對，請點擊連結註冊帳號\nhttps://partner.bitget.fit/bg/WedJatBTC\n然后輸入正確的 UID""")


async def remind_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("欢迎使用！请使用 /start 命令开始对话。")

if __name__ == '__main__':
    app = Application.builder().token(constants.TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
                    
    app.run_polling(poll_interval=3)
