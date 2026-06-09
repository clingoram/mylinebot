import requests
from django.conf import settings
import time

LINE_API_URL = "https://api.line.me/v2/bot/channel/webhook/endpoint"


def get_ngrok_url():
    try:
        res = requests.get(
            "http://127.0.0.1:4040/api/tunnels",
            timeout=3
        )

        tunnels = res.json().get("tunnels", [])

        for tunnel in tunnels:
            if tunnel["proto"] == "https":
                return tunnel["public_url"]

    except Exception as e:
        print("取得ngrok URL失敗:", e)

    return None

def wait_ngrok(retry=10):
    import requests

    for i in range(retry):
        try:
            res = requests.get("http://127.0.0.1:4040/api/tunnels", timeout=2)
            tunnels = res.json().get("tunnels", [])

            for t in tunnels:
                if t["proto"] == "https":
                    return t["public_url"]

        except Exception:
            pass

        time.sleep(1)

    return None

def update_line_webhook():
    ngrok_url = get_ngrok_url()

    if not ngrok_url:
        print("找不到ngrok tunnel")
        return

    callback_url = f"{ngrok_url}/callback/"

    headers = {
        "Authorization": f"Bearer {settings.LINE_CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    res = requests.put(
        LINE_API_URL,
        headers=headers,
        json={
            "endpoint": callback_url
        }
    )

    print("status:", res.status_code)
    print("response:", res.text)


    if res.status_code == 200:
        print(f"LINE Webhook 已更新: {callback_url}")
    else:
        print("LINE Webhook 更新失敗")
        print(res.text)