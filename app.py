import telebot
from flask import Flask

TOKEN = "8852863411:AAHJeN2b7oHdWedNjG1wTb0uNYSSgs3JK4A"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot Running 🚀")

@app.route("/")
def home():
    return "Bot Running"

if __name__ == "__main__":
    bot.infinity_polling()
