from django.http import HttpResponse
from django.conf import settings
import re
from urllib.parse import parse_qs

from linebot import LineBotApi
from linebot.models import TextSendMessage,TextMessage,FlexSendMessage

from apps.stock.services.quotes import get_stock_flex_message
from apps.stock.services.tracking import follow_stock,unfollow_stock,get_user_stocks_list
from apps.stock.models import FavoriteStock
from apps.basic_info.models import Person

LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

# =========================
# Public
# =========================
def handle_stock_data(event): 
    '''
    取得單一股票
    '''
    # userId = event.source.user_id 
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

    '''
     person = Person.objects.get(user_account=userId)
        exist_or_not = FavoriteStock.objects.filter(user_account=person,stock_id=stock).exists() 
    
        if action == "watch" and stock and exist_or_not == False: 
            follow_stock(userId,stock) 
            LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=f"已加入追蹤：{stock}")) 
        elif action == "unfollow" and stock and exist_or_not == True: 
            unfollow_stock(userId,stock) 
            LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=f"取消追蹤：{stock}")) 
        else: 
            LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text="參數錯誤"))
    
    '''
    if not action or not stock:
        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text="參數錯誤"))
        return

    try:
        person = Person.objects.get(user_account=userId)
    except Person.DoesNotExist:
        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text="找不到使用者"))
        return

    exist_or_not = FavoriteStock.objects.filter(user_account=person,stock_id=stock).exists()

    if action == "watch":
        if exist_or_not:
            LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=f"已經追蹤：{stock}"))
            return

        follow_stock(userId, stock)

        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=f"已加入追蹤：{stock}"))

    elif action == "unfollow":
        if not exist_or_not:
            LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=f"目前沒有追蹤：{stock}"))
            return

        unfollow_stock(userId, stock)

        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=f"取消追蹤：{stock}"))

    else:
        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text="參數錯誤"))

def handle_followlist(event):
    '''
    處理追蹤清單
    '''
    userId = event.source.user_id
    result = get_user_stocks_list(userId)
    LINE_BOT_API.reply_message(event.reply_token,FlexSendMessage(alt_text = "追蹤清單",contents=result))
    return HttpResponse("OK!!",status=200)