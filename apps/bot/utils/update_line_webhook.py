'''
抓ngrok + 更新LINE webhook

'''
import time
import requests
import os

LINE_API = "https://api.line.me/v2/bot/channel/webhook/endpoint"
NGROK_API = "http://127.0.0.1:4040/api/tunnels"

LINE_CHANNEL_ACCESS_TOKEN = os.getenv(
    "LINE_CHANNEL_ACCESS_TOKEN"
)

def get_ngrok_url():
    '''
    取ngrok URL
    '''
    res = requests.get(NGROK_API, timeout=2)
    tunnels = res.json().get("tunnels", [])

    for t in tunnels:
        if t["proto"] == "https":
            return t["public_url"]

    return None


def wait_ngrok(retry=30, delay=1):
    '''
    ngrok還沒ready會自動等
    webhook更新失敗會重試
    '''
    for i in range(retry):
        url = get_ngrok_url()
        if url:
            return url

        time.sleep(delay)

    raise RuntimeError("ngrok not ready after waiting")


def update_line_webhook():
    '''
    更新line webhook url
    '''
    url = wait_ngrok()

    print("💡 ngrok url=", url)

    if not url:
        print("沒抓到ngrok")
        return

    # 組合成webhook URL
    callback_url = f"{url}/callback"

    print("💡 callback=", callback_url)
    print("🔑 token=", LINE_CHANNEL_ACCESS_TOKEN[:10] + "...")
    print("❓ token valid=", bool(LINE_CHANNEL_ACCESS_TOKEN))
    print("📏 token length=", len(LINE_CHANNEL_ACCESS_TOKEN or ""))

    headers = {
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    # 呼叫LINE API更新webhook
    res = requests.put(
        LINE_API,
        headers=headers,
        json={"endpoint": callback_url},
        timeout=5
    )
    print(res)
    print("status=", res.status_code)
    print("response=", res.text)