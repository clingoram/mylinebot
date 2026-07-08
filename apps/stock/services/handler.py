from django.http import HttpResponse
from django.conf import settings
import re
from urllib.parse import parse_qs

from linebot import LineBotApi
from linebot.models import TextSendMessage,TextMessage,FlexSendMessage

from apps.stock.services.quotes import get_stock_flex_message
from apps.stock.services.tracking import follow_stock,unfollow_stock,get_user_stocks_message

LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def handle_stock_data(event): 
    '''
    取得單一股票
    '''
    userId = event.source.user_id 
    # 只保留數字0-9 
    keyWord = re.findall(r"\d+", event.message.text)[0]
    numbers = get_stock_flex_message(keyWord)
    
    if not numbers:
        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text="請輸入股票代號"))
        return
    
    LINE_BOT_API.reply_message(event.reply_token,FlexSendMessage(alt_text = keyWord + f"追蹤 {keyWord}",contents=numbers)) 
    
    return HttpResponse("OK!!",status=200)

def handle_postback(event):
    '''
    按下 
    追蹤 (股票代碼)
    或
    取消追蹤 (股票代碼)
    '''
    userId = event.source.user_id
    data = event.postback.data

    params = parse_qs(data)

    action = params.get("action", [None])[0]
    stock = params.get("stock_id", [None])[0]

    if action == "watch" and stock:
        follow_stock(userId,stock)

        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=f"已加入追蹤：{stock}"))
    else:
        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text="參數錯誤"))

    if action == "unfollow" and stock:
        unfollow_stock(userId,stock)
        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=f"取消追蹤：{stock}"))

def handle_followlist(event):
    '''
    處理追蹤清單
    '''
    userId = event.source.user_id
    result = get_user_stocks_message(userId)
    LINE_BOT_API.reply_message(event.reply_token,FlexSendMessage(alt_text = "清單",contents=result))
    return HttpResponse("OK!!",status=200)