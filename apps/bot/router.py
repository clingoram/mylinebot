from django.conf import settings
from django.http import HttpResponse

from apps.basic_info.models import Person,Message
from apps.basic_info.services.actions import create_user,create_Keyword
from apps.basic_info.services.explain import explain

from apps.bot.services.parse_command import parse_command
from apps.bot.services.line_reply import reply

from apps.news.services.handle_news import handle_news
from apps.weather.services.handle_weather import handle_weather

from apps.stock.services.handler import handle_stock_data,handle_postback,handle_followlist

from linebot.models import PostbackEvent,TextSendMessage



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
        create_Keyword(user_id=userId,keyword=keyWord)
        if not Person.objects.filter(user_account=userId).exists():
          # 建立person(user)
          create_user(userId=userId)

        command = parse_command(text = keyWord)

        if command["action"] == "weather":
          # 氣象
          handle_weather(event=event,location=command["city"])

        elif command["action"] == "stock":
          # 股票
          handle_stock_data(event=event,stock_id=command["stock_code"])

        elif command["action"] == "news":
          # 新聞
          handle_news(event=event,keyword=command["keyword"],category=command["category"])

        elif command["action"] == "follow_list":
          # 列出 股票追蹤清單
          handle_followlist(event=event)

        elif command["action"] == "explain":
          # 說明
          explain(event=event)

        elif command["action"] == "unknown":
          reply(event.reply_token,TextSendMessage("發生操作錯誤，詳見「說明」"))


      elif isinstance(event, PostbackEvent):
        # 追蹤或取消追蹤
        handle_postback(event=event)

    return HttpResponse("OK",status=200)