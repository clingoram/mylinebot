'''
抓ngrok + 更新LINE webhook
'''
import time
import requests
import os

LINE_API = "https://api.line.me/v2/bot/channel/webhook/endpoint"
NGROK_API = os.getenv("NGROK_API_URL")

def get_ngrok_url():
    '''
    取ngrok URL
    '''
    try:
        res = requests.get(NGROK_API, timeout=2)
        res.raise_for_status()

        tunnels = res.json().get("tunnels", [])

        for t in tunnels:
            if t.get("proto") == "https":
                return t.get("public_url")

    except requests.RequestException:
        return None

    return None


def wait_ngrok(retry=30, delay=1):
    '''
    ngrok還沒準備好會自動等
    webhook更新失敗會重試
    '''
    for i in range(retry):
        url = get_ngrok_url()
        if url:
            return url

        time.sleep(delay)

    raise RuntimeError("☹️ ngrok還沒準備好")


def update_line_webhook():
    '''
    更新line webhook url
    '''
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    if not LINE_CHANNEL_ACCESS_TOKEN:
        raise RuntimeError("☹️ 沒拿到LINE_CHANNEL_ACCESS_TOKEN")
    
    try:
        url = wait_ngrok()
    except Exception as e:
        print("☹️ 沒抓到ngrok", e)
        return
    print("💡 ngrok url =", url)

    # 組合成webhook URL
    callback_url = f"{url}/callback"

    print("💡 callback =", callback_url)
    print("🔑 token =", LINE_CHANNEL_ACCESS_TOKEN[:3] + "...")
    print("❓ token valid =", bool(LINE_CHANNEL_ACCESS_TOKEN))
    print("📏 token length =", len(LINE_CHANNEL_ACCESS_TOKEN or ""))

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

    if res.ok:
        print("✅ Webhook Updated")
    else:
        print("❌ Update Failed")
        print("status =" , res.status_code)
        print("response =", res.text)