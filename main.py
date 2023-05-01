from telegram.ext import *
import telegram.ext

async def start(update, context):
 await update.message.reply_text("Welcome to NBA tweets")

async def help(update, context): await update.message.reply_text(
            """
 /start ->  Welcome to the channel
 /help -> Okay we will help
 /content -> see the tweeps we bring you their tweets
        """)

async def handle_message(update, context):
 await update.message.reply_text(f"You said {update.message.text}, use the commands using /")
async def content(update, context):
 await update.message.reply_text("twitter link : https://twitter.com/espn/status/1652123221913640960?s=20")
 Token = ("6120960014:AAHF_GkKZDxm-xBnLpENnUUqzKJm5bqs5Xg")
application = Application.builder().token("6120960014:AAHF_GkKZDxm-xBnLpENnUUqzKJm5bqs5Xg").build()
application.add_handler(telegram.ext.CommandHandler('start', start))
application.add_handler(telegram.ext.CommandHandler('help', help))
application.add_handler(telegram.ext.CommandHandler('content', content))
application.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.Text, handle_message))
application.run_polling()
    # application.idle()

