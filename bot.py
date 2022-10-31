import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, f"Привет,{message.from_user.first_name}")



@bot.message_handler(commands = ['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton
    ("Посетить вебсайт", url = 'https://itcbootcamp.com'))
    bot.send_message(message.chat.id,"перейти на сайт", reply_markup = markup)  

@bot.message_handler()
def get_user_text(message):
    if message.text == "hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode = 'html')
    
    # elif message.text == 'photo':
    #     photo = open('1122.jpg','rb')
    #     bot.send_photo(message.chat.id, photo)

    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Ваш ID:{message.from_user.id}", parse_mode ='html')

    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю ", parse_mode = 'html')

@bot.message_handler(content_types = ['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Хахаха")

def t():
    pass


# @bot.message_handler(commands = ['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()

#     markup.add(types.InlineKeyboardButton
#     ("Посетить вебсайт", url = 'https://itcbootcamp.com'))
#     bot.send_message(message.chat.id,"перейти на сайт", reply_markup = markup)        

bot.polling(non_stop=True)