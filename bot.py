import logging
from telegram.ext import Updater, CommandHandler, MessageHandler

logging.basicConfig(level=logging.INFO)

TOKEN = '7546434205:AAGN7aIVMB8VI63eU_udN6PMB7nLzyllluw'  # Replace with your bot's API token
AUTH_USERS = ['5265276618']  # Replace with your user ID
CHAT_IDS = []  # List to store chat IDs

def add_group(update, context):
    if update.effective_user.id in AUTH_USERS:
        message = update.message.text
        if message.startswith('/addgroup '):
            chat_id = message.replace('/addgroup ', '')
            if chat_id.isdigit():
                CHAT_IDS.append(int(chat_id))
                update.message.reply_text(f'Chat ID {chat_id} added successfully.')
            else:
                update.message.reply_text('Invalid chat ID.')
        else:
            update.message.reply_text('Please enter a chat ID to add.')
    else:
        update.message.reply_text('You are not authorized to use this command.')

def broadcast_message(update, context):
    if update.effective_user.id in AUTH_USERS:
        message = update.message.text
        if message.startswith('/broadcast '):
            broadcast_text = message.replace('/broadcast ', '')
            for chat_id in CHAT_IDS:
                context.bot.send_message(chat_id=chat_id, text=broadcast_text)
        else:
            update.message.reply_text('Please enter a message to broadcast.')
    else:
        update.message.reply_text('You are not authorized to use this command.')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('addgroup', add_group))
    dp.add_handler(CommandHandler('broadcast', broadcast_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
