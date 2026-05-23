import telebot

TOKEN = "8852863411:AAHJeN2b7oHdWedNjG1wTb0uNYSSgs3JK4A"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send Video URL")

@bot.message_handler(func=lambda m: True)
def get_link(message):

    video_url = message.text

    mx_link = f"""
Open In MX Player👇

intent://{video_url}#Intent;package=com.mxtech.videoplayer.ad;end
"""

    bot.reply_to(message, mx_link)

print("Bot Started...")
bot.infinity_polling()
