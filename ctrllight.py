from telegram.ext import Updater,CommandHandler # importing the required functions from telegram library of python
from Adafruit_IO import Client,Feed,Data   # Importing the the required function from Adafruit library
import os   #operating system

x = os.getenv('ADAFRUIT_IO_USERNAME')   # adafruit username and password should be given as 'Config Vars' in the settings of your app on Heroku 
y = os.getenv('ADAFRUIT_IO_KEY')
aio = Client(x,y) # Calling the username and the key into a single variable aio
TELEGRAM= os.getenv('TELEGRAM_KEY')  # telegram bot key is fed to the variable telegram from which the input and output is recieved
# function to send values to adafruit.io
def value_send(value):
  feed = aio.feeds('ctrllight') # feed crtllight is called from the above mentioned username
  aio.send_data(feed.key,value)  # data value or updated value is sent to the adafruit server

# function when /lighton is sent via the bot
def On(bot, update):
  chat_id = update.message.chat_id #updating the particular chat id
  bot.send_message(chat_id, text="Lights ON") #Sending message to the user that lights are switched on
  bot.send_photo(chat_id, photo='https://images.app.goo.gl/EgmisKBLpz82bHqv6') #Sending a image to the user showing that the lights are on
  value_send(1)# value sent to the value_send function
#function when /lightoff is sent via the bot
def Off(bot, update):
  chat_id = update.message.chat_id #particular chat id id updated 
  bot.send_message(chat_id, text="Lights OFF") # Returning message to the user tha lights are switched off
  bot.send_photo(chat_id,photo='https://images.app.goo.gl/BLFdTFJ9TsJ3okD49') #Sending the image to the user showing that the lights are turned off
  value_send(0) # value is sent to the value_send function

u = Updater(TELEGRAM) #the updater method is used to update the value
dp = u.dispatcher #here the output is dipatched to the user
dp.add_handler(CommandHandler('lighton',On))# command hadler to handle the command given by the user
dp.add_handler(CommandHandler('lightoff',Off)) #command hadler to handle the command given by the user
u.start_polling()
u.idle() # idle fuction to keep everything idle if the input is not given
