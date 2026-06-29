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
    # print(handleEvent)
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

        
        # if keyWord.startswith(("股票","stock","Stock","台股","臺股")):
        #   return handle_stock_data(event)

        # if keyWord.startswith("追蹤","follow"):
        #   return userFollow(userId)

        if keyWord in ["股票","stock","Stock","台股","臺股","追蹤","follow"]:
          return handle_stock_data(event)

        return HttpResponse("OK!!",status=200)
    return HttpResponse("Not allowed", status=405)
    '''
    
    for event in handleEvent:
      # 如果有事件
      if isinstance(event,MessageEvent):
        userId = event.source.user_id
        profile = LINE_BOT_API.get_profile(userId)
        name = profile.display_name
        keyWord = event.message.text

        # 新增關鍵字至資料表
        insertKeyWord(profile.user_id,keyWord)

        message=[]

        # 新聞爬蟲
        if keyWord == "新聞" or keyWord == "news":
          crawler = crawlerSomething()
          LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text=crawler))
           
        elif keyWord == "功能列表":
          rich_menu = LINE_BOT_API.get_rich_menu(settings.RICH_MENU)
          LINE_BOT_API.reply_message(event.reply_token,FlexSendMessage(alt_text='FlexMessage',contents=flex_message))
        

        # 搜尋天氣資訊
        elif keyWord[-1] == "市" or keyWord[-1] == "縣":
          weatherResult = flex_message(keyWord)
          if weatherResult:
            LINE_BOT_API.reply_message(event.reply_token,FlexSendMessage(alt_text = keyWord + "氣象資訊",contents=weatherResult)) 
          else:
            LINE_BOT_API.reply_message(event.reply_token,TextSendMessage(text = keyWord + "不在可搜尋範圍內。可搜尋: "+",".join(city())))

        if not Person.objects.filter(uid=userId).exists():
          # 建立person(user)
          create_user(userId,name)
          message.append(TextSendMessage(text="資料新增完畢"))

    return HttpResponse("OK!!",status=200)
    '''
    
    