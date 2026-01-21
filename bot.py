import telebot

bot = telebot.TeleBot("8595115985:AAEQInFhoQI-yUs3kmSIYjmuDPW65ufmO1o")
MY_LINK = "https://jeannettaleath-ship-it.github.io/MAX191/"

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "مرحباً بك في EROXX. أرسل صورتك لدمجها مع رابط التتبع.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    [span_4](start_span)bot.reply_to(message, "📄 تم تلقيم صورتك بنجاح[span_4](end_span)!")
    bot.send_message(message.chat.id, f"💡 أرسل هذا الرابط لهاتفك الآخر:\n{MY_LINK}")

bot.polling()
