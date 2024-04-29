# from sys import exception
from email import message
from logging import basicConfig
from unicodedata import numeric
from urllib import request
from django.shortcuts import render

from bot.flexMsg import flex_message
from basic_info.views import insertKeyWord,create_user
from crawler.views import crawlerSomething

# Create your views here.
from django.http import HttpResponse
import requests
from basic_info.models import Person,Message

import json,base64,hashlib,hmac,re
import numpy as np
from datetime import datetime, timedelta

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

# line bot
from linebot import LineBotApi
from linebot.webhook import WebhookParser,WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage,TextMessage,FlexSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
# handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

# @handler.add(MessageEvent, message=TextMessage)
@csrf_exempt
def handle_message(request):
  if request.method == "POST":
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')

    # hash = hmac.new(line_bot_api.encode('utf-8'),body.encode('utf-8'), hashlib.sha256).digest()
    # signature = base64.b64encode(hash)
    try:
      # 傳入事件
      handleEvent = parser.parse(body, signature)
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

        if keyWord == 'info':
          print(keyWord)
          crawler = crawlerSomething()
          print(crawler)
          # botInformation = line_bot_api.get_bot_info()
          # print(botInformation)

          # line_bot_api.reply_message(i.reply_token,botInformation)
          
        # if keyWord == "功能列表":
        #   rich_menu = get_rich_menu(settings.RICH_MENU)
        #   flexMessage = flex_message()
        #   line_bot_api.reply_message(i.reply_token,FlexSendMessage(alt_text='FlexMessage',contents=flexMessage))
      
        # message=[]
        # if not Person.objects.filter(uid=id).exists():
        #   # 建立person(user)
        #   # person = Person.objects.create(uid=id, account=name, created_at=datetime.now())
        #   # person.save()
        #   create_user(id,name)

        #   message.append(TextSendMessage(text='資料新增完畢'))
        #   # line_bot_api.reply_message(i.reply_token, message)

        # if keyWord[-1] == "市" or keyWord[-1] == "縣":
        #   # insertKeyWord(profile.user_id,keyWord)  
        #   print(profile.user_id,keyWord)

        #   weatherResult = flex_message(keyWord)
          # line_bot_api.reply_message(i.reply_token,FlexSendMessage(alt_text=keyWord+"氣象資訊",contents=weatherResult)) 
          # dump = json.dumps(weatherResult).encode('utf-8').decode('unicode-escape')

    return HttpResponse()
  else:
    return HttpResponseBadRequest()