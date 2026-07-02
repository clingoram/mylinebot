from django.conf import settings
from django.http import HttpResponse

from apps.basic_info.models import Person,Message
from apps.basic_info.services.create_user import create_user
from apps.basic_info.services.create_keyword import insertKeyWord

from apps.crawler.services.handle_news import handle_news
from apps.weather.services.handle_weather import handle_weather
from apps.stock.services.handle_stock_data import handle_stock_data
# from apps.stock.services.user_follow import userFollow


from linebot.models import MessageEvent,TextSendMessage
from linebot import LineBotApi
LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def route_event(handleEvent):
    '''
    bot.views.py to bot.router 
    分流
    '''
    for event in handleEvent:
      if isinstance(event, MessageEvent):
        userId = event.source.user_id
        # profile = LINE_BOT_API.get_profile(userId)
        # userName = profile.display_name
        keyWord = event.message.text

        message=[]

        # 新增關鍵字至資料表
        insertKeyWord(userId,keyWord)

        if not Person.objects.filter(account=userId).exists():
          # 建立person(user)
          create_user(userId)
          # message.append(TextSendMessage(text="資料新增完畢"))

        if keyWord in ["新聞", "news","News","NEWS"]:
          return handle_news(event)

        if keyWord.endswith(("市", "縣")):
          return handle_weather(event)

        
        if keyWord.startswith(("股票","stock","Stock","台股","臺股","追蹤","follow")):
          return handle_stock_data(event)

        # if keyWord.startswith("追蹤","follow"):
        #   return userFollow(userId)

        # if keyWord in ["股票","台股","臺股","追蹤","follow"]:
        #   return handle_stock_data(event)

      return HttpResponse("OK!!",status=200)
    return HttpResponse("Not allowed", status=405)