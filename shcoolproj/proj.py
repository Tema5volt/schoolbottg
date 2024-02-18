import telebot
from telebot import types # для указание типов
from background immport keep_alive
token='6318964337:AAGzXDdA4vF5QToMCsglMAdrdRRYLEVzF7c'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📐Математика")
    btn2 = types.KeyboardButton("📘Русский")
    btn3 = types.KeyboardButton("🧲Физика")
    markup.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Привет! Это бот который покажет тебе справочные материалы по твоему предмету за 10 класс".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "📐Математика"):
        bot.send_message(message.chat.id, text="Держи справочные материалы по математике за 10 класс!")
        photo1 = open('math1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        photo2 = open('math2.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
    elif(message.text == "📘Русский"):
        bot.send_message(message.chat.id, "Держи справочные материалы по русскому за 10 класс")
        # bot.send_photo(chat_id, "rus1.jpg")
        photo3 = open('rus1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo3)
    elif(message.text == "🧲Физика"):
        bot.send_message(message.chat.id, "Держи справочные материалы по физике за 10 класс")
        photo4 = open('phys1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo4)
    else:
        bot.send_message(message.chat.id, text="Извини, на такое ответить не могу")

bot.polling(none_stop=True)