
import asyncio
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

    # while True:
    #     time.sleep(1)
    #     recibido = bot.get_updates()
    #     request_data = recibido[len(recibido)-1]
    #     chat_id = request_data.message.chat_id
    #     msg_current = request_data.message.text
    #     bot.send_message(chat_id, msg_current)
    #     # print(request_data)
    #     if msg_current == 'terminar':
    #         break


if __name__ == '__main__':
    asyncio.run(main())



    
# {'update_id': 451297745, 'message': {'group_chat_created': False, 'caption_entities': [], 
# 'delete_chat_photo': False, 
# 'chat': {'username': 'arabeltz', 'first_name': 'Moor', 'id': 1822798056, 'last_name': 'Mood', 'type': 'private'}, 
# 'new_chat_photo': [], 
# 'date': 1662247580, 
# 'new_chat_members': [], 
# 'entities': [], 
# 'message_id': 2, 
# 'channel_chat_created': False, 
# 'text': 'hola', 
# 'photo': [], 
# 'supergroup_chat_created': False, 
# 'from': {'id': 1822798056, 'first_name': 'Moor', 'username': 'arabeltz', 'language_code': 'es', 'is_bot': False, 'last_name': 'Mood'}}}
