from django.http import HttpResponse
import re
from apps.stock.services.get_stock import getStock
from apps.stock.services.flex import flex
from apps.stock.services.user_follow import userFollowList

from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage,TextMessage,FlexSendMessage

from urllib.parse import parse_qs

LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


# def handle_stock_data(event):
#     # 只保留數字0-9
#     result = getStock(re.findall(r"\d+", event.message.text)[0])
#     LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=result))

#     return HttpResponse("OK!!",status=200)


def handle_stock_data(event):
    # TODO:此涵式須加上使用者追蹤股票功能.尚未完成
    
    userId = event.source.user_id
    keyWord = event.message.text

    # 只保留數字0-9
    result = flex(re.findall(r"\d+", keyWord)[0])
    # result = getStock(re.findall(r"\d+", keyWord)[0])
    # LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=result))
    LINE_BOT_API.reply_message(event.reply_token,FlexSendMessage(alt_text = keyWord + "追蹤",contents=result)) 


    return HttpResponse("OK!!",status=200)



def handle_postback(event):
    user_id = event.source.user_id
    data = event.postback.data

    params = parse_qs(data)

    action = params.get("action", [None])[0]
    stock = params.get("stock", [None])[0]

    if action == "watch":
        userFollowList(user_id, stock)
        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=f"已加入追蹤：{stock}"))