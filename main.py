from flask import Flask, request
import telebot
import os

TOKEN = "7697675014:AAEbeOmjJ83JQcw47Ydzgveqh2ecp3GtUnA"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# لیست پیام‌ها و پاسخ‌های خودکار
auto_replies = {
    "شرایط": """✨ شرایط سفارش ایموجی:
برای اینکه سفارشتون رو با اطمینان شروع کنیم، ۳۰٪ از مبلغ سفارش رو به عنوان پیش‌پرداخت دریافت می‌کنیم.
این کار باعث میشه بتونیم طراحی رو با خیال راحت شروع کنیم و مطمئن بشیم که نظرتون قطعیه. 🙌

بعد از ثبت سفارشتون:
✅ ایموجی‌ها طراحی میشن.
✅ پیش‌نمایش براتون ارسال میشه تا رنگ و شکل کلی رو تأیید کنید.
✅ بعد از تأیید، مابقی مبلغ رو پرداخت می‌کنید و لینک پک ایموجی براتون ارسال میشه.

✅ اگه با شرایط موافقید، فقط کلمه "سفارش" رو بفرستید تا لینک فرم اطلاعات براتون ارسال بشه.

ممنون که به ما اعتماد دارید❤️""",

    "قیمت": """💰 قیمت ایموجی‌ها:
🔹 هر ایموجی ۸۰ هزار تومان
🔹 مثال: پک ۳تایی = ۲۴۰ هزار تومان

🎉 آفر ویژه:
اگه سفارش شما بیشتر از ۸ ایموجی باشه، ۲۰٪ تخفیف شامل حالتون میشه! 😍
⏳ این تخفیف محدوده، پس اگه قصد سفارش دارید، پیشنهاد می‌کنم این فرصت رو از دست ندید.

✅ اگه از شرایط سفارش خبر ندارید، کافیه کلمه "شرایط" رو ارسال کنید تا اطلاعات کامل براتون ارسال بشه.""",

    "سفارش": """📋 فرم سفارش:
حالا که با شرایط و قیمت‌ها آشنا شدید، لطفاً این فرم رو با دقت پر کنید تا سفارشتون سریع‌تر و بدون مشکل انجام بشه. 👇
[فرم سفارش](https://docs.google.com/forms/d/e/1FAIpQLSf9iZTBtZBl-O2xeTFwnr07csSXenYQXeoUoLy1sVFRsgqr1Q/viewform?usp=dialog)

ممنون که همراه ما هستید❤️"""
}

@app.route("/", methods=["GET"])
def home():
    return "ربات فعال است! ✅"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    if update:
        bot.process_new_updates([telebot.types.Update.de_json(update)])
    return "OK", 200

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    text = message.text.strip()
    if text in auto_replies:
        bot.reply_to(message, auto_replies[text], parse_mode="Markdown")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
