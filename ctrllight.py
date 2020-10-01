from Adafruit_IO import Client, Feed,Data
from telegram.ext import Updater,CommandHandler
import os
ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')   # adafruit username and password should be given as 'Config Vars' in the settings of your app on Heroku 
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
aio = Client('ADAFRUIT_IO_USERNAME','ADAFRUIT_IO_KEY') # create instance of REST client
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')  # similar to the adafruit username and password


def valcloud(value):
  to_feed = aio.feeds('ctrllight') # put youctrllightr own feed name here
  aio.send_data(to_feed.key,value)  # append a new value to a feed

# function to switch on light and send value '1' to adafruit
def On(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Lights ON")
  bot.send_photo(chat_id, photo='https://www.securityroundtable.org/wp-content/uploads/2019/03/AdobeStock_261504199-scaled.jpeg')
  valcloud(1)
#function to switch off the light and send value '0' to adafruit
def Off(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Lights OFF")
  bot.send_photo(chat_id=update.effective_chat.id,photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')
  valcloud(0)

u = Updater('TELEGRAM_TOKEN',use_context = True) 
dp = u.dispatcher
dp.add_handler(CommandHandler('lighton',On))  # register a handler
dp.add_handler(CommandHandler('lightoff',Off))
u.start_polling()  # starts polling updates from Telegram
u.idle() # blocks until one of the signals are received and stops the updater
