import requests
import json
import subprocess
from linebot import LineBotApi
from linebot.webhook import WebhookParser
from django.conf import settings


# LINE Webhook 更新API
LINE_API_URL = "https://api.line.me/v2/bot/channel/webhook/endpoint"
line_bot_token = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

def get_ngrok_url():
    # 讀ngrok API，本機端口4040會自動提供
    try:
        res = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = res.json()["tunnels"]
        for tunnel in tunnels:
            if tunnel["proto"] == "https":
                return tunnel["public_url"]
    except Exception as e:
        print("無法取得ngrok URL:", e)
    return None

def update_line_webhook(url):
    headers = {
        "Authorization": f"Bearer {line_bot_token}",
        "Content-Type": "application/json"
    }
    data = {"endpoint": url}
    res = requests.put(LINE_API_URL, headers=headers, data=json.dumps(data))
    if res.status_code == 200:
        print("Webhook 更新成功:", url)
    else:
        print("Webhook 更新失敗:", res.status_code, res.text)

if __name__ == "__main__":
    ngrok_url = get_ngrok_url()
    if ngrok_url:
        callback_url = f"{ngrok_url}/callback/"
        update_line_webhook(callback_url)
    else:
        print("找不到ngrok HTTPS URL")