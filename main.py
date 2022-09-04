import logging
from telegram import Update
from telegram.ext import filters,ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import Config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#Este es el comando start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Bienvenido al Bot")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

if __name__ == '__main__':
    application = ApplicationBuilder().token(Config.M.MY_TOKEN_BOT).build()
    
    start_handler = CommandHandler('start', start)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)


    application.add_handler(start_handler)

    application.add_handler(echo_handler)
    
    application.run_polling()

# import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# application = ApplicationBuilder().token('5688833678:AAFFVG7lLa5wvJmlXyLMoeCw9BFjD6xoL-U').build()

# if __name__ == '__main__':
#     asyncio.run(main())

# {'update_id': 451297761, 'message': {'supergroup_chat_created': False, 'delete_chat_photo': False, 
# 'channel_chat_created': False, 'text': 'terminar', 'date': 1662270341, 'caption_entities': [], 'chat': {'last_name': 'Mood', 'type': 'private', 'username': 'arabeltz', 'first_name': 'Moor', 'id': 1822798056}, 'new_chat_photo': [], 'message_id': 182, 'group_chat_created': False, 'photo': [], 'entities': [], 'new_chat_members': [], 'from': {'first_name': 'Moor', 'last_name': 'Mood', 'language_code': 'es', 'username': 'arabeltz', 'is_bot': False, 'id': 1822798056}}}

