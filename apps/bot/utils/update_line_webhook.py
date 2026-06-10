'''
因為ngrok每次重開，URL都會改變
自動將ngrok所產生的網址更新到LINE Bot Webhook
'''
import time
import requests
from django.conf import settings

LINE_API = "https://api.line.me/v2/bot/channel/webhook/endpoint"
NGROK_API = "http://127.0.0.1:4040/api/tunnels"

def get_ngrok_url():
    '''
    找ngrok URL
    '''
    res = requests.get(NGROK_API, timeout=2)
    tunnels = res.json().get("tunnels", [])

    for t in tunnels:
        if t["proto"] == "https":
            return t["public_url"]

    return None


def wait_ngrok(retry=10):
    '''
    ngrok還沒ready會自動等
    webhook更新失敗會重試
    '''
    for _ in range(retry):
        url = get_ngrok_url()
        if url:
            return url
        time.sleep(1)
    return None


def update_line_webhook():
    url = wait_ngrok()

    print("ngrok url=", url)

    if not url:
        print("沒抓到ngrok")
        return

    # 組合成webhook URL
    callback_url = f"{url}/callback/"

    print("callback=", callback_url)
    print("token=", settings.LINE_CHANNEL_ACCESS_TOKEN[:10], "...")
    print("token valid=", bool(settings.LINE_CHANNEL_ACCESS_TOKEN))
    print("token length=", len(settings.LINE_CHANNEL_ACCESS_TOKEN or ""))

    headers = {
        "Authorization": f"Bearer {settings.LINE_CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    # 呼叫LINE API更新 webhook
    res = requests.put(
        LINE_API,
        headers=headers,
        json={"endpoint": callback_url},
        timeout=5
    )

    print("status=", res.status_code)
    print("response=", res.text)