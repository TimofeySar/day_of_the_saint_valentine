from flask import Flask, render_template, redirect, url_for
import os
import requests
import time
import threading
app = Flask(__name__)

def ping_self():
    while True:
        try:
            requests.get("https://your-render-app.onrender.com")
        except Exception as e:
            print("Ping failed:", e)
        time.sleep(300)  # Пинг каждые 5 минут

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task1', methods=['GET', 'POST'])
def task1():
    return render_template('task1.html')


@app.route('/task2', methods=['GET', 'POST'])
def task2():
    return render_template('task2.html')


@app.route('/task3', methods=['GET', 'POST'])
def task3():
    return render_template('task3.html')


@app.route('/final')
def final():
    return render_template('final.html')


if __name__ == '__main__':
    threading.Thread(target=ping_self, daemon=True).start()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
