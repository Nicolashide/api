import telebot
TOKEN = "828754275:AAEjbgAFxd0go8JHdw5cnMryfzgQbuwZnuM"
bot = telebot.TeleBot(TOKEN)
 
# Приветственная надпись
@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)
 
def hello(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
 
bot.infinity_polling(True)
