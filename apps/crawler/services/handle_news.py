from django.conf import settings
from apps.crawler.services.crawler import crawlerSomething
from cityList import city
from linebot.models import MessageEvent, TextSendMessage,TextMessage,FlexSendMessage
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden


from linebot import LineBotApi
LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def handle_news(event):
    '''
    將得到的資料塞進line bot內
    '''
    result = crawlerSomething()

    LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=result))

    return HttpResponse("OK!!",status=200)
            