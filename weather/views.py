# from sys import exception
from logging import basicConfig
from urllib import request
from django.shortcuts import render

from weather.flexMsg import flex_message
# from weather.weather import weatherAPI

# Create your views here.
from django.http import HttpResponse
import requests
from info.models import Person,Message

import json
import base64
import hashlib
import hmac
import re
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
        # if i.message.text == "功能列表":
        #   rich_menu = get_rich_menu(settings.RICH_MENU)
        #   flexMessage = flex_message()
        #   line_bot_api.reply_message(i.reply_token,FlexSendMessage(alt_text='FlexMessage',contents=flexMessage))

        id = i.source.user_id
        profile = line_bot_api.get_profile(id)
        name = profile.display_name
        keyWord = i.message.text
      
        message=[]
        if not Person.objects.filter(uid=id).exists():
            # 建立person(user)
            Person.objects.create(uid=id, account=name, created_at=datetime.now())
      
            message.append(TextSendMessage(text='資料新增完畢'))
            line_bot_api.reply_message(i.reply_token, message)


        if i.message.text[-1] == "市" or i.message.text[-1] == "縣":
          if Person.objects.get(uid=id):
            # 將user message存到message
            person = Person.objects.get(uid=id)
            person.updated_at = datetime.now()
            person.save()

            # msg = Person.objects.get(uid=id)
            msg = Message.objects.create(uid=id, contentKeyWord = keyWord)
            # (uid=id, contentKeyWord = keyWord)
            msg.save()

            # message.append(TextSendMessage(text='新增完畢'))
          # line_bot_api.reply_message(i.reply_token, message)              

          weatherResult = flex_message(i.message.text)
          line_bot_api.reply_message(i.reply_token,FlexSendMessage(alt_text=i.message.text+"氣象資訊",contents=weatherResult)) 
            # dump = json.dumps(weatherResult).encode('utf-8').decode('unicode-escape')

    return HttpResponse()
  else:
    return HttpResponseBadRequest()
