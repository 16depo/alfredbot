import telegram
from telegram.ext import Updater, CommandHandler
import logging

def start(bot, update):
    depobot.send_message(chat_id=update.message.chat_id, text="Good evening, sir, do you want me to prepare some tea?")
def sendip(bot, update):
    ipfile=open('/home/depo/externalIP', 'r')
    ip=str(ipfile.read())
    depobot.send_message(chat_id=update.message.chat_id, text="Home current IP is "+ip)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
bot_token=''
depobot=telegram.Bot(token=bot_token)
updater=Updater(token=bot_token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

ip_handler = CommandHandler('showip',sendip)
dispatcher.add_handler(ip_handler)

updater.start_polling()
