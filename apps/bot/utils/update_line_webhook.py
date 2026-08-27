'''
抓ngrok + 更新LINE webhook
'''
import time
import requests
import os
import logging
logger = logging.getLogger(__name__)

def get_ngrok_url():
    '''
    取ngrok URL
    '''
    NGROK_API = os.getenv("NGROK_API_URL")

    if not NGROK_API:
        logger.warning("❌ NGROK API URL沒設定")
        return None
    try:
        res = requests.get(NGROK_API, timeout=2)
        res.raise_for_status()

        tunnels = res.json().get("tunnels", [])

        for t in tunnels:
            if t.get("proto") == "https":
                return t.get("public_url")

    except requests.RequestException:
        logger.exception("NGROK requests發生錯誤")
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


def update_line_webhook(retry=5, delay=2):
    '''
    更新line webhook url
    '''
    LINE_API = "https://api.line.me/v2/bot/channel/webhook/endpoint"
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

    if not LINE_CHANNEL_ACCESS_TOKEN:
        raise RuntimeError("☹️ 沒拿到LINE CHANNEL TOKEN")
    
    try:
        url = wait_ngrok()
    except Exception as e:
        logger.exception(f"☹️ 沒抓到ngrok {e}")
        return
    
    logger.info(f"💡 ngrok url = {url}")

    # 組成webhook URL
    callback_url = f"{url}/callback"

    # print("🔑 token =", LINE_CHANNEL_ACCESS_TOKEN[:3] + "...")

    token_valid_check = "是" if bool(LINE_CHANNEL_ACCESS_TOKEN) else "否"

    logger.info(f"💡 callback = {callback_url}")
    logger.info(f"❓ token是否有效 = {token_valid_check}")

    headers = {
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    # 最多試5次，5次都失敗就會跑到raise RuntimeError("☹️ ngrok還沒準備好")
    for i in range(retry):
        try:
            logger.info(f"🔄 更新LINE Webhook ({i + 1}/{retry})")

            res = requests.put(
                LINE_API,
                headers=headers,
                json={"endpoint": callback_url},
                timeout=5,
            )

            if res.ok:
                logger.info("✅ Webhook Updated")
                return

            logger.warning(f"❌ LINE Webhook更新失敗")
            # logger.error(f"status = {res.status_code}")
            # logger.error(f"response = {res.text}")

            if res.status_code in (400, 401, 403):
                return

        except requests.RequestException as e:
            logger.exception(f"LINE API連線失敗：{e}")

        if i < retry - 1:
            time.sleep(delay)

    logger.warning("LINE Webhook更新失敗，已達最大重試次數")