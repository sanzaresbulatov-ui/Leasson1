import telebot
import random
import os
import requests
bot = telebot.TeleBot("8333984025:AAFe0QbFReUfJUuvX2cDY7g7vcgqK1Oc7Gs")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Вот все команды: /mem /duck /animal /start")


@bot.message_handler(commands=['mem'])
def send_mem(message):
    img = random.choice(os.listdir("images"))
    with open(f'images/{img}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)


@bot.message_handler(commands=['animal'])
def send_animal(message):
    img = random.choice(os.listdir("animals"))
    with open(f'animals/{img}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  
    


bot.polling()
