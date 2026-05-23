import telebot

TOKEN = "8852863411:AAHJeN2b7oHdWedNjG1wTb0uNYSSgs3JK4A"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send Video 🎬")

@bot.message_handler(content_types=['video','document'])
def video(message):

    if message.video:
        file_id = message.video.file_id
    else:
        file_id = message.document.file_id

    file_info = bot.get_file(file_id)

    download_link = f"""
https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}
"""

    bot.reply_to(
        message,
        f"Direct Link ✅\n\n{download_link}"
    )

print("Bot Started...")
bot.infinity_polling()
