from telegram import Update
from telegram.ext import (
    Application,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    filters
)
from AI import AI

application = Application.builder().token("5969830322:AAF-Ki5HmN2fqy8H1nnugeLMQQIB_3WC_es").build()
print("Successfully connected to Telegram API")
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Mister Platypus at your Service")

application.add_handler(CommandHandler('start', start))

async def mimic(update: Update, context: CallbackContext):
    incoming_text = update.message.text
    AI(incoming_text)
    await update.message.reply_text("Command Executed Successfully")

application.add_handler(MessageHandler(filters=filters.TEXT, callback=mimic))

application.run_polling()