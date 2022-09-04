
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
    # 
    mensaje_actual = ['0', 0]

    while True:
        time.sleep(1)
        recibido = bot.get_updates()
        request_data = recibido[len(recibido)-1]
        chat_id = request_data.message.chat_id
        msg_current = request_data.message.text
        fecha_msg = request_data.message.date
        print(chat_id)

        if mensaje_actual[1] <= 0 and msg_current == 'terminar':
            mensaje_actual[0] = fecha_msg
            mensaje_actual[1] = 1

        if fecha_msg != mensaje_actual[0]:
            if msg_current == 'terminar' and fecha_msg != mensaje_actual[0]:
                print(msg_current[0], str(fecha_msg))
                bot.send_message(chat_id, config.MSG_FINISH)
                break
            bot.send_message(chat_id, msg_current)
            mensaje_actual[0] = fecha_msg
        # print(request_data)


if __name__ == '__main__':
    asyncio.run(main())

# {'update_id': 451297761, 'message': {'supergroup_chat_created': False, 'delete_chat_photo': False, 
# 'channel_chat_created': False, 'text': 'terminar', 'date': 1662270341, 'caption_entities': [], 'chat': {'last_name': 'Mood', 'type': 'private', 'username': 'arabeltz', 'first_name': 'Moor', 'id': 1822798056}, 'new_chat_photo': [], 'message_id': 182, 'group_chat_created': False, 'photo': [], 'entities': [], 'new_chat_members': [], 'from': {'first_name': 'Moor', 'last_name': 'Mood', 'language_code': 'es', 'username': 'arabeltz', 'is_bot': False, 'id': 1822798056}}}

