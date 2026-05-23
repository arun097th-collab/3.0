import telebot

TOKEN = "8852863411:AAHJeN2b7oHdWedNjG1wTb0uNYSSgs3JK4A"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send 2GB Video 🎬")

@bot.message_handler(content_types=['video','document'])
def save_video(message):

    file_id = (
        message.video.file_id
        if message.video
        else message.document.file_id
    )

    bot.reply_to(message, f"Saved ✅\n\n{file_id}")

bot.infinity_polling()
