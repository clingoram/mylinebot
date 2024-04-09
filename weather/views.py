from urllib import request
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests

import json
import base64
import hashlib
import hmac

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

# line bot
from linebot import LineBotApi
from linebot.webhook import WebhookParser,WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage,TextMessage
'''
MessageEvent (信息事件)FollowEvent (加好友事件)、UnfollowEvent (刪好友事件)、JoinEvent (加入聊天室事件)、LeaveEvent (離開聊天室事件)、MemberJoinedEvent (加入群組事件)、MemberLeftEvent (離開群組事件)
'''


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
# handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

# Create your views here.
@csrf_exempt
def callbackLine(request):
    '''
    line bot
    '''
    if request.method == 'POST':
      signature = request.META['HTTP_X_LINE_SIGNATURE']
      body = request.body.decode('utf-8')

      # hash = hmac.new(line_bot_api.encode('utf-8'),body.encode('utf-8'), hashlib.sha256).digest()
      # signature = base64.b64encode(hash)

      try:
        events = parser.parse(body, signature)
      except InvalidSignatureError:
        return HttpResponseForbidden()
      except LineBotApiError:
        return HttpResponseBadRequest()

      for event in events:
        if isinstance(event, MessageEvent):
          mtext=event.message.text
          message=[]
          message.append(TextSendMessage(text=mtext))
          line_bot_api.reply_message(event.reply_token,message)

      return HttpResponse()
    else:
      return HttpResponseBadRequest()


def weatherAPI(location:str):
    '''
    氣象局API
    '''
    # if request.method == "GET":
      # location = input('Enter query location: ')
    # print(location)
    response = requests.get('https://goweather.herokuapp.com/weather/'+location)
    # response = requests.get('https://jsonplaceholder.typicode.com/todos/'+ int(id[0]))#+location)

    response.raise_for_status()
    if response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json"):
      data = response.json()
      return data['temperature']
          # print(json_object['temperature'],json_object['wind'],json_object['description'])

          # for i in json_object["forecast"]:
          #   print(i["day"],i['temperature'],i['wind'])

      # for key,value in data.items():
        # print(key,value)
        # return key
      # return HttpResponse('EG')
    pass

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
        if i.message.text == "功能列表":
           # 回復「功能列表」按鈕樣板訊息
          line_bot_api.reply_message(i.reply_token,Featuresmodel().content())

        if i.message.text == "天氣":
          weatherResult = weatherAPI(i.message.text)
          # for key,value in weatherResult.items():
          #   # print(key,value)

          # line_bot_api.reply_message(i.reply_token,TextSendMessage(text=i.message.text))
          line_bot_api.reply_message(i.reply_token,TextSendMessage(text=weatherResult))

    return HttpResponse()
  else:
    return HttpResponseBadRequest()
