import telebot
import os

token = '5814884989:AAGzD3cRDpIc1bJhKMBFMuLSOmRPRSVSTKU'
bot = telebot.TeleBot(token, parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Ready to use...")

@bot.message_handler(func=lambda message: True)
def get_pictures(message):
	if message.text == 'get pic':
		os.system('main.py')
		photo=open('cam.png','rb')
		bot.send_photo(message.chat.id,photo)

bot.infinity_polling()