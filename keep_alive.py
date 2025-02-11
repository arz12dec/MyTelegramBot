from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "من زنده‌ام!"

def keep_alive():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
