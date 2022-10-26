import telebot
from telebot import types
from thifr import thifrtel

bot = telebot.TeleBot('Ваш тег')

@bot.message_handler(commands=['start'])
def start(massage):
    bot.send_message(massage.chat.id, "Этот бот поддерживает шифровку и расшифровку символов русского и англиского языка (в нижнем регистре) и некоторых знаков припенания!")


@bot.message_handler(commands=['encrypt'])
def thif(message):
    b = [Id пользователей]
    a = message.from_user.id
    cn = 0
    for i in b:
        if i == a:
            cn += 1
    if cn == 0:       
        bot.send_message(message.chat.id,"К сожалению этот бот приватный!")
    if cn == 1:        
        s = bot.reply_to(message, "Что нужно зашифровать?")
        bot.register_next_step_handler(s, th)

def th(message):
    try:
        message_to_save = message.text
        message_to_save = message_to_save.lower()
        message_to_save = str(message_to_save)
        a = message_to_save
        b = thifrtel.thif(a)
        x = b
        bot.send_message(message.chat.id, x)
    except:
        bot.send_message(message.chat.id, "Данные введены некорректно")            

@bot.message_handler(commands=['decrypt'])
def thif(message):
    b = [Id Пользователей]
    a = message.from_user.id
    cn = 0
    for i in b:
        if i == a:
            cn += 1
    if cn == 0:       
        bot.send_message(message.chat.id,"К сожалению этот бот приватный!")
    if cn == 1:        
        s = bot.reply_to(message, "Что нужно расшифровать?")
        bot.register_next_step_handler(s, t)    

def t(message):
    try:
        message_to_save = message.text
        message_to_save = message_to_save.lower()
        message_to_save = str(message_to_save)

        #print(message_to_save)
        c = message_to_save
        d = thifrtel.sh(c)
        e = d
        bot.send_message(message.chat.id, e)
    except:
        bot.send_message(message.chat.id, "Данные введены некорректно")
bot.polling(none_stop=True)