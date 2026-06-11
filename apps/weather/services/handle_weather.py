from django.conf import settings
from apps.weather.services.flexMsg import flex_message
from cityList import city
from linebot.models import MessageEvent, TextSendMessage,TextMessage,FlexSendMessage
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden

from linebot import LineBotApi
LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def handle_weather(event):
    '''
    將得到的資料塞進line bot內
    '''
    result = flex_message(event.message.text)

    if result:
        LINE_BOT_API.reply_message(event.reply_token,FlexSendMessage(alt_text = event.message.text + "氣象資訊",contents=result)) 
    else:
        LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text = event.message.text + "不在可搜尋範圍內。可搜尋: "+",".join(city())))

    return HttpResponse("OK!!",status=200)
            