from django.http import HttpResponse
from django.conf import settings
from urllib.parse import parse_qs
import re
# from linebot import LineBotApi
from linebot.models import TextSendMessage,TextMessage,FlexSendMessage

from apps.bot.services.line_reply import reply
from apps.stock.services.quotes import get_stock_flex_message,_clean_stock_id
from apps.stock.services.tracking import follow_stock,unfollow_stock,get_user_stocks_list
from apps.stock.models import FavoriteStock
from apps.basic_info.models import Person

# LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

# =========================
# Public
# =========================
def handle_stock_data(event,stock_id) -> None: 
    '''
    取得單一股票
    '''
    #只取英文大小寫和數字
    keyWord = re.sub(r"[^a-zA-Z0-9]", "", stock_id).upper()
    result = get_stock_flex_message(stock_id)
    
    if not result:
        reply(event.reply_token,TextSendMessage("請輸入股票代號"))
        return
    
    reply(event.reply_token,FlexSendMessage(alt_text = keyWord + f"追蹤 {keyWord}",contents = result))
    # return HttpResponse("OK!!",status=200)

def handle_followlist(event) -> None:
    '''
    顯示追蹤清單
    '''
    userId = event.source.user_id
    result = get_user_stocks_list(userId)
    reply(event.reply_token,FlexSendMessage(alt_text = "追蹤清單",contents=result))
    # return HttpResponse("OK!!",status=200)
    
def handle_postback(event) -> None:
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

    if not action or not stock:
        reply(event.reply_token,TextSendMessage("參數錯誤"))
        return

    try:
        person = Person.objects.get(user_account=userId)
    except Person.DoesNotExist:
        reply(event.reply_token,TextSendMessage("找不到使用者"))
        return

    exist_or_not = FavoriteStock.objects.filter(user_account=person,stock_id=stock).exists()

    if action == "watch":
        if exist_or_not:
            reply(event.reply_token,TextSendMessage(f"已經追蹤：{stock}"))
            return

        follow_stock(userId, stock)

        reply(event.reply_token,TextSendMessage(f"已加入追蹤：{stock}"))

    elif action == "unfollow":
        if not exist_or_not:
            reply(event.reply_token,TextSendMessage(f"目前沒有追蹤：{stock}"))
            return

        unfollow_stock(userId, stock)

        reply(event.reply_token,TextSendMessage(f"取消追蹤：{stock}"))

    else:
        reply(event.reply_token,TextSendMessage("參數錯誤"))