from flask import Flask
from replit import web  # اینجا برای استفاده از سرور Replit اضافه میشه

app = Flask(__name__)

@app.route('/')
def home():
    return "من زنده‌ام"  # وقتی وارد URL بشی این رو نمایش میده

def keep_alive():
    web.run(app)  # این خط برای اجرای سرور روی WebView در Replit است