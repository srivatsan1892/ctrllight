from Adafruit_IO import Client, Feed,Data
from telegram.ext import Updater,CommandHandler
import os
ADAFRUIT_IO_USERNAME =os.getenv('ADAFRUIT_IO_USERNAME')
ADAFRUIT_IO_KEY =os.getenv('ADAFRUIT_IO_KEY')
aio = Client('ADAFRUIT_IO_USERNAME','ADAFRUIT_IO_KEY')


def cloudval(value):
  feed=aio.feeds('ctrllight')
  aio.send_data(feed.key,value)
def On(bot,update):
  chat_id=update.message.chat_id
  bot.send_message(chat_id,"Lights On")
  bot.send_photo(chat_id, photo='https://images.app.goo.gl/EgmisKBLpz82bHqv6')
  cloudval(1)
def Off(bot,update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Lights OFF")
  bot.send_photo(chat_id,photo='https://images.app.goo.gl/BLFdTFJ9TsJ3okD49')
  cloudval(0)
  

u = Updater('1191554053:AAGsZs6ntwJ6mziPYkcFEtI5LItsbjdzxLI') 
dp = u.dispatcher
dp.add_handler(CommandHandler('lighton',lighton))  
dp.add_handler(CommandHandler('lightoff',lightoff))

u.start_polling() 
u.idle()
