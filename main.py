
import asyncio
from email.policy import default
import telegram
import Config as c
import time

config = c.M

async def main():
    '''Configuracion del robot'''
    bot = telegram.Bot(config.MY_TOKEN_BOT)
    # lista  = list(bot.get_updates())
    # print(lista[0])
    # bot.send_message(config.MY_USER_ID, 'Hello')
    # 
    mensaje_actual = ['0', 0]
    # writer = open('./BotTg/db.txt', 'w')

    while True:
        time.sleep(1)
        reader = open('./BotTg/db.txt')
        recibido = bot.get_updates()
        request_data = recibido[len(recibido)-1]
        chat_id = request_data.message.chat_id
        msg_current = request_data.message.text
        id_msg = request_data.message.message_id

        match msg_current:
            case '/start':
                if (readers := open('./BotTg/db.txt').readlines()[0]) != str(id_msg) and msg_current != 'terminar':
                    writer = open('./BotTg/db.txt', 'w')
                    writer.write(str(id_msg))
                    writer.close()
                    bot.send_message(config.MY_USER_ID, 'Bienvenido a Bot Telegram')
            case 'terminar':
                if reader.read(10) != str(id_msg) and msg_current == 'terminar':
            # print('File: ' + str(reader.read(30)) + ' Server: ' + str(id_msg))
                    writer = open('./BotTg/db.txt', 'w')
            # print(request_data.message.message_id)
                    writer.write(str(id_msg))
                    writer.close()
            case _:
                if (readers := open('./BotTg/db.txt').readlines()[0]) != str(id_msg) and msg_current != 'terminar':
                    writer = open('./BotTg/db.txt', 'w')
                    writer.write(str(id_msg))
                    writer.close()
                    bot.send_message(config.MY_USER_ID, msg_current)


if __name__ == '__main__':
    asyncio.run(main())

# {'update_id': 451297761, 'message': {'supergroup_chat_created': False, 'delete_chat_photo': False, 
# 'channel_chat_created': False, 'text': 'terminar', 'date': 1662270341, 'caption_entities': [], 'chat': {'last_name': 'Mood', 'type': 'private', 'username': 'arabeltz', 'first_name': 'Moor', 'id': 1822798056}, 'new_chat_photo': [], 'message_id': 182, 'group_chat_created': False, 'photo': [], 'entities': [], 'new_chat_members': [], 'from': {'first_name': 'Moor', 'last_name': 'Mood', 'language_code': 'es', 'username': 'arabeltz', 'is_bot': False, 'id': 1822798056}}}

