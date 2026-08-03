from django.conf import settings
from django.http import HttpResponse

from apps.basic_info.models import Person,Message
from apps.basic_info.services.actions import create_user,create_Keyword

from apps.crawler.services.handle_news import handle_news
from apps.weather.services.handle_weather import handle_weather

from apps.stock.services.handler import handle_stock_data,handle_postback,handle_followlist

from linebot.models import PostbackEvent
from linebot import LineBotApi
LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def route_event(handleEvent):
    '''
    bot.views.py to bot.router 
    分流
    '''
    for event in handleEvent:
      if event.type == "message" and event.message.type == "text":
        userId = event.source.user_id
        # profile = LINE_BOT_API.get_profile(userId)
        # userName = profile.display_name
        keyWord = event.message.text

        message=[]

        # 新增關鍵字至資料表
        create_Keyword(userId,keyWord)

        if not Person.objects.filter(user_account=userId).exists():
          # 建立person(user)
          create_user(userId)
          # message.append(TextSendMessage(text="資料新增完畢"))

        if keyWord in ["新聞", "news","News","NEWS"]:
          return handle_news(event)

        if keyWord.endswith(("市", "縣")):
          return handle_weather(event)

        if keyWord.startswith(("股票","stock","Stock","台股","臺股")):
          return handle_stock_data(event)
        
        if keyWord in ["我的股票","追蹤清單"]:
          return handle_followlist(event)

      elif isinstance(event, PostbackEvent):
        return handle_postback(event)

    return HttpResponse("OK!!",status=200)