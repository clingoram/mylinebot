from django.conf import settings
from django.http import HttpResponse

from apps.bot.services.parse_command import parse_command

from apps.basic_info.models import Person,Message
from apps.basic_info.services.actions import create_user,create_Keyword
from apps.basic_info.services.explain import explain

from apps.crawler.services.handle_news import handle_news
from apps.weather.services.handle_weather import handle_weather

from apps.stock.services.handler import handle_stock_data,handle_postback,handle_followlist
from linebot.models import PostbackEvent


def route_event(handleEvent):
    '''
    分流
    '''
    for event in handleEvent:
      if event.type == "message" and event.message.type == "text":
        userId = event.source.user_id

        keyWord = event.message.text

        # message=[]
        # 新增關鍵字至資料表
        create_Keyword(userId,keyWord)
        if not Person.objects.filter(user_account=userId).exists():
          # 建立person(user)
          create_user(userId)

        command = parse_command(keyWord)

        if command["action"] == "weather":
          # 氣象
          handle_weather(event,command["city"])

        elif command["action"] == "stock":
          # 股票
          handle_stock_data(event,command["stock_code"])

        elif command["action"] == "news":
          # 爬蟲新聞
          handle_news(event,command["keyword"],command["category"])

        elif command["action"] == "follow_list":
          # 股票追蹤清單
          handle_followlist(event)

        elif command["action"] == "explain":
          # 說明
          explain(event)


      elif isinstance(event, PostbackEvent):
        handle_postback(event)

    return HttpResponse("OK",status=200)

      #   # 新增關鍵字至資料表
      #   create_Keyword(userId,keyWord)
      #   if not Person.objects.filter(user_account=userId).exists():
      #     # 建立person(user)
      #     create_user(userId)
      #     # message.append(TextSendMessage(text="資料新增完畢"))
      #   if keyWord in ["新聞", "news","News","NEWS","爬蟲"]:
      #     handle_news(event)

      #   if keyWord.endswith(("市", "縣")):
      #     handle_weather(event)
      #   if keyWord.startswith(("股票","stock","Stock","台股","臺股")):
      #     handle_stock_data(event)
        
      #   if keyWord in ["我的股票","追蹤清單"]:
      #     handle_followlist(event)

      # elif isinstance(event, PostbackEvent):
      #   handle_postback(event)

      # return HttpResponse("OK!!",status=200)