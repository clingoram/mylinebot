from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .router import handle_message

@csrf_exempt
def callback(request):
    text = request.body.decode("utf-8")

    reply = handle_message(text)

    return HttpResponse(reply)

'''
from logging import basicConfig
from unicodedata import numeric
from urllib import request
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

# import function
from apps.bot.flexMsg import flex_message
from apps.basic_info.views import insertKeyWord,create_user
from apps.crawler.views import crawlerSomething
from cityList import city
# import model
from apps.basic_info.models import Person,Message

import requests

import json,base64,hashlib,hmac,re
import numpy as np
from datetime import datetime, timedelta

# line bot
from linebot import LineBotApi
from linebot.webhook import WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError,BaseError
from linebot.models import MessageEvent, TextSendMessage,TextMessage,FlexSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def handle_message(request):
  if request.method == "POST":
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
      # 傳入事件
      handleEvent = parser.parse(body, signature)
    except BaseError:
      return "發生錯誤"
    except InvalidSignatureError:
      return HttpResponseForbidden()
    except LineBotApiError:
      return HttpResponseBadRequest()

    for i in handleEvent:
      # 如果有事件
      if isinstance(i,MessageEvent):
        id = i.source.user_id
        profile = line_bot_api.get_profile(id)
        name = profile.display_name
        keyWord = i.message.text

        message=[]
        # 新聞爬蟲
        if keyWord == "新聞" or keyWord == "news":
          crawler = crawlerSomething()
          line_bot_api.reply_message(i.reply_token,TextSendMessage(text=crawler))
          
        # if keyWord == "功能列表":
        #   rich_menu = line_bot_api.get_rich_menu(settings.RICH_MENU)
        #   line_bot_api.reply_message(i.reply_token,FlexSendMessage(alt_text='FlexMessage',contents=flexMessage))
      
        if not Person.objects.filter(uid=id).exists():
          # 建立person(user)
          create_user(id,name)
          message.append(TextSendMessage(text="資料新增完畢"))


        # 搜尋天氣資訊
        if keyWord[-1] == "市" or keyWord[-1] == "縣":
          weatherResult = flex_message(keyWord)
          if bool(weatherResult):
           line_bot_api.reply_message(i.reply_token,FlexSendMessage(alt_text = keyWord + "氣象資訊",contents=weatherResult)) 
          else:
            line_bot_api.reply_message(i.reply_token,TextSendMessage(text = keyWord + "不在可搜尋範圍內。可搜尋: "+",".join(city())))

        # 新增關鍵字至資料表
        insertKeyWord(profile.user_id,keyWord)
    return HttpResponse()
  else:
    return HttpResponseBadRequest()
'''