import telebot

TOKEN = "8852863411:AAHJeN2b7oHdWedNjG1wTb0uNYSSgs3JK4A"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot Running 🚀")

print("Bot Started...")
bot.infinity_polling()
