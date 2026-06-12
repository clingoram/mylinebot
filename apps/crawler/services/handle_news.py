from django.conf import settings
from apps.crawler.services.crawler import crawlerSomething
from linebot.models import TextSendMessage
from django.http import HttpResponse


from linebot import LineBotApi
LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def handle_news(event):
    '''
    將得到的資料塞進line bot內
    '''
    result = crawlerSomething()

    LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=result))

    return HttpResponse("OK!!",status=200)
            