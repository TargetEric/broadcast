import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

logging.basicConfig(level=logging.INFO)

TOKEN = '7546434205:AAGN7aIVMB8VI63eU_udN6PMB7nLzyllluw'  # Replace with your bot's API token
AUTH_USERS = ['5265276618']  # Replace with your user ID
CHAT_IDS = []  # List to store chat IDs

async def add_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id in AUTH_USERS:
        message = update.message.text
        if message.startswith('/addgroup '):
            chat_id = message.replace('/addgroup ', '')
            if chat_id.isdigit():
                CHAT_IDS.append(int(chat_id))
                await update.message.reply_text(f'Chat ID {chat_id} added successfully.')
            else:
                await update.message.reply_text('Invalid chat ID.')
        else:
            await update.message.reply_text('Please enter a chat ID to add.')
    else:
        await update.message.reply_text('You are not authorized to use this command.')

async def broadcast_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id in AUTH_USERS:
        message = update.message.text
        if message.startswith('/broadcast '):
            broadcast_text = message.replace('/broadcast ', '')
            for chat_id in CHAT_IDS:
                await context.bot.send_message(chat_id=chat_id, text=broadcast_text)
        else:
            await update.message.reply_text('Please enter a message to broadcast.')
    else:
        await update.message.reply_text('You are not authorized to use this command.')

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', lambda update, context: update.message.reply_text('Welcome to the broadcast bot!'))
    add_group_handler = CommandHandler('addgroup', add_group)
    broadcast_handler = CommandHandler('broadcast', broadcast_message)

    application.add_handler(start_handler)
    application.add_handler(add_group_handler)
    application.add_handler(broadcast_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
