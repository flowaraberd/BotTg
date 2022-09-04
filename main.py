
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
