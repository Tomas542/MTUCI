import telebot
from telebot import types
from random import randint

token = '0'
bot = telebot.TeleBot(token)
count = 0

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", "Ping", "/cats")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/cats", "Ping", "/start")
    bot.send_message(message.chat.id, 'Список того, на что я способен:'
                        '\n/start - первая команда пользователя здоровается и предлагает узнать про МТУСИ'
                         '\n/help - Вывод данного сообщения и добавление большинства команд в быстрый доступ'
                        '\n/cat - Фотография кота '
                        '\n\nТакже со мной можно поиграть в пинг-понг (ping) (или bang, чтобы сразу забить)'
                                      '\nИли сказать хочу, чобы узнать про МТУСИ', reply_markup=keyboard)

@bot.message_handler(commands=['cats'])
def cat(message):
    random_id = randint(0, 5)
    if random_id == 0:
        bot.send_photo(message.chat.id, "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.VLr2dH4FMo9fakdC6QoB-wEsCo%26pid%3DApi&f=1")
    elif random_id == 1:
        bot.send_photo(message.chat.id, "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fmymodernmet.com%2Fwp%2Fwp-content%2Fuploads%2F2017%2F03%2Fgabrielius-khiterer-stray-cats-11.jpg&f=1&nofb=1")
    elif random_id == 2:
        bot.send_photo(message.chat.id, "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhddesktopwallpapers.in%2Fwp-content%2Fuploads%2F2015%2F09%2Fcute-cats-download.jpg&f=1&nofb=1")
    elif random_id == 3:
        bot.send_photo(message.chat.id, "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Friotfest.org%2Fwp-content%2Fuploads%2F2019%2F05%2Fgrumpy-cat.jpg&f=1&nofb=1")
    elif random_id == 4:
        bot.send_photo(message.chat.id, "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.gexU2H9w2PRLTr5Cgk-f2QHaHa%26pid%3DApi&f=1")
    elif random_id == 5:
        bot.send_photo(message.chat.id, "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.212eAc7IFRrnzooFvyctlQHaFj%26pid%3DApi&f=1")

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "ping":
        bot.send_message(message.chat.id, "pong")
    if message.text.lower() == "bang":
        bot.send_message(message.chat.id, "You got point. You won!)")

bot.polling(non_stop=True)


