from django.conf import settings
from apps.crawler.services.crawler import crawler_news
from apps.bot.services.line_reply import reply
from linebot.models import TextSendMessage
from django.http import HttpResponse

from linebot import LineBotApi
LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def handle_news(event) -> HttpResponse:
    '''
    將得到的新聞爬蟲資料塞進line bot內
    '''
    result = crawler_news()
    print(result)

    reply(event.reply_token,TextSendMessage(text=result))

    return HttpResponse("OK!!",status=200)
            