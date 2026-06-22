from django.http import HttpResponse
import re
from apps.stock.services.get_stock import getStock
from apps.stock.services.user_follow import userFollow

from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage
LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


# def handle_stock_data(event):
 
#     # 只保留數字0-9
#     result = getStock(re.findall(r"\d+", event.message.text)[0])
#     LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=result))

#     return HttpResponse("OK!!",status=200)


def handle_stock_data(event):
    
    userId = event.source.id
    profile = LINE_BOT_API.get_profile(userId)
    userName = profile.display_name
    keyWord = event.message.text

    if keyWord.startswith(("股票","stock","Stock","台股","臺股")):
        # 只保留數字0-9
        result = getStock(re.findall(r"\d+", keyWord)[0])
        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=result))

    elif keyWord.startswith("追蹤","follow","收藏"):
        result = userFollow(userId)

    return HttpResponse("OK!!",status=200)