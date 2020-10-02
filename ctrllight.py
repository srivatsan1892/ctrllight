from telegram.ext import Updater,CommandHandler # import the required handlers from telegram.ext package
from Adafruit_IO import Client,Feed,Data   # import the libraries to create feeds and send data to it
import os   #operating system

x = os.getenv('ADAFRUIT_IO_USERNAME')   # adafruit username and password should be given as 'Config Vars' in the settings of your app on Heroku 
y = os.getenv('ADAFRUIT_IO_KEY')
aio = Client(x,y) # create instance of REST client
TELEGRAM= os.getenv('TELEGRAM_TOKEN')  # similar to the adafruit username and password
# function to send values to adafruit.io
def value_send(value):
  to_feed = aio.feeds('ctrllight') # put your own feed name here
  aio.send_data(to_feed.key,value)  # append a new value to a feed

# function to switch on light and send value '1' to adafruit
def lighton(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Light has been turned ON")
  bot.send_photo(chat_id, photo='https://www.securityroundtable.org/wp-content/uploads/2019/03/AdobeStock_261504199-scaled.jpeg')
  value_send(1)
#function to switch off the light and send value '0' to adafruit
def lightoff(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Light has been turned OFF")
  bot.send_photo(chat_id,photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')
  value_send(0)

u = Updater(TELEGRAM)
dp = u.dispatcher
dp.add_handler(CommandHandler('lighton',lighton))
dp.add_handler(CommandHandler('lightoff',lightoff))
u.start_polling()
u.idle() 
