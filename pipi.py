import requests
import time
while True:
    try:
        response = requests.get("https://your-render-app.onrender.com")
        print("Ping successful:", response.status_code)
    except Exception as e:
        print("Ping failed:", e)
    time.sleep(300)  # Пинг каждые 5 минут (300 секунд)