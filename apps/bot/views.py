from apps.bot.router import route_event
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot.exceptions import InvalidSignatureError, LineBotApiError,BaseError
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from linebot.webhook import WebhookParser
LINE_WEBHOOK_PARSER = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def handle_message(request):
  if request.method == 'POST':
    body = request.body.decode('utf-8')
    signature = request.META['HTTP_X_LINE_SIGNATURE']

    try:
      # 傳入事件
      handleEvent = LINE_WEBHOOK_PARSER.parse(body, signature)
    except BaseError:
      return "發生錯誤"
    except InvalidSignatureError:
      return HttpResponseForbidden()
    except LineBotApiError:
      return HttpResponseBadRequest()
    
    return route_event(handleEvent)
  else:
    return HttpResponse("Method not allowed", status=405)
  
'''
from logging import basicConfig
from unicodedata import numeric
from urllib import request
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

# import function
# from apps.bot.flexMsg import flex_message
from apps.basic_info.views import insertKeyWord,create_user
from apps.crawler.views import crawlerSomething
from cityList import city
# import model
from apps.basic_info.models import Person,Message

# line bot
from linebot import LineBotApi
from linebot.webhook import WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError,BaseError
from linebot.models import MessageEvent, TextSendMessage,TextMessage,FlexSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def handle_message(request):
 
  if request.method == 'POST':
    body = request.body.decode('utf-8')
    signature = request.META['HTTP_X_LINE_SIGNATURE']

    try:
      # 傳入事件
      handleEvent = parser.parse(body, signature)
    except BaseError:
      return "發生錯誤"
    except InvalidSignatureError:
      return HttpResponseForbidden()
    except LineBotApiError:
      return HttpResponseBadRequest()

    for event in handleEvent:
      # 如果有事件
      if isinstance(event,MessageEvent):
        userId = event.source.user_id
        profile = line_bot_api.get_profile(userId)
        name = profile.display_name
        keyWord = event.message.text

        # 新增關鍵字至資料表
        insertKeyWord(profile.user_id,keyWord)

        message=[]

        # 新聞爬蟲
        if keyWord == "新聞" or keyWord == "news":
          crawler = crawlerSomething()
          line_bot_api.reply_message(event.reply_token,TextSendMessage(text=crawler))
           
        elif keyWord == "功能列表":
          rich_menu = line_bot_api.get_rich_menu(settings.RICH_MENU)
          line_bot_api.reply_message(event.reply_token,FlexSendMessage(alt_text='FlexMessage',contents=flex_message))
        

        # 搜尋天氣資訊
        elif keyWord[-1] == "市" or keyWord[-1] == "縣":
          weatherResult = flex_message(keyWord)
          if weatherResult:
            line_bot_api.reply_message(event.reply_token,FlexSendMessage(alt_text = keyWord + "氣象資訊",contents=weatherResult)) 
          else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = keyWord + "不在可搜尋範圍內。可搜尋: "+",".join(city())))

        if not Person.objects.filter(uid=userId).exists():
          # 建立person(user)
          create_user(userId,name)
          message.append(TextSendMessage(text="資料新增完畢"))

    return HttpResponse("OK!!",status=200)
  
  else:
    return HttpResponse("Method not allowed", status=405)
'''