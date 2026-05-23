import telebot

TOKEN = "8852863411:AAHJeN2b7oHdWedNjG1wTb0uNYSSgs3JK4A"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send Video 🎬")

@bot.message_handler(content_types=['video', 'document'])
def video(message):

    try:
        file_id = message.video.file_id if message.video else message.document.file_id

        file_info = bot.get_file(file_id)

        file_path = file_info.file_path

        download_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

        bot.reply_to(message, "Download Link 👇\n" + download_url)

    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

print("Bot Started...")
bot.infinity_polling()
