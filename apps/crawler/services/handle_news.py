from django.conf import settings
from apps.crawler.services.text_news import create_news_text
from apps.bot.services.line_reply import reply
from linebot.models import TextSendMessage
from django.http import HttpResponse

def handle_news(event,keyword = None,category= None) -> HttpResponse:
    '''
    將得到的新聞爬蟲資料塞進line bot內
    '''
    result = create_news_text(keyword,category)

    reply(event.reply_token,TextSendMessage(text=result))
            