
import telebot

TOKEN = 8182408107:AAE_2xLrlF8qG7k5Xwmy8cnCClarBqU3S7I

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    teclado = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    teclado.add("?? Camisas", "?? Cal�ados")
    bot.send_message(message.chat.id, "Ol�! Escolha uma op��o:", reply_markup=teclado)

@bot.message_handler(func=lambda msg: msg.text == "?? Camisas")
def camisas(msg):
    bot.send_message(msg.chat.id, "Camisas por R$130\nFornecedor: https://wa.me/SEUNUMERO1")

@bot.message_handler(func=lambda msg: msg.text == "?? Cal�ados")
def calcados(msg):
    bot.send_message(msg.chat.id, "Cal�ados por R$120\nFornecedor: https://wa.me/SEUNUMERO2")

print("Bot rodando...")
bot.infinity_polling()
