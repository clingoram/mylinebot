# from sys import exception
from logging import basicConfig
from urllib import request
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests

import json
import base64
import hashlib
import hmac
import re

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
weather_api = settings.WEATHER_ACCESS_TOKEN

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
# handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

# Create your views here.
# @csrf_exempt
# def callbackLine(request):
#     '''
#     line bot
#     '''
#     if request.method == 'POST':
#       signature = request.META['HTTP_X_LINE_SIGNATURE']
#       body = request.body.decode('utf-8')

#       # hash = hmac.new(line_bot_api.encode('utf-8'),body.encode('utf-8'), hashlib.sha256).digest()
#       # signature = base64.b64encode(hash)

#       try:
#         events = parser.parse(body, signature)
#       except InvalidSignatureError:
#         return HttpResponseForbidden()
#       except LineBotApiError:
#         return HttpResponseBadRequest()

#       for event in events:
#         if isinstance(event, MessageEvent):
#           mtext=event.message.text
#           message=[]
#           message.append(TextSendMessage(text=mtext))
#           line_bot_api.reply_message(event.reply_token,message)

#       return HttpResponse()
#     else:
#       return HttpResponseBadRequest()


def weatherAPI(location:str):
      '''
      氣象局API(一般天氣預報，今明36小時天氣預報)
      1.城市名稱須完整顯示縣或市，例如高雄市、宜蘭縣。
      2.城市名稱必須是繁體字。
      3.若無城市名稱，預設為全部縣市
      '''
      # if request.method == "GET":
      location = input('Enter query location: ')

      cityList = ["宜蘭縣","花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣", "臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", "基隆市", "新竹縣", "新竹市", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "嘉義市", "屏東縣"]
      # sililarCityList = ["嘉義縣", "嘉義市","新竹縣", "新竹市"]

      if location != "":
        # 替換簡體字
        # 若location非none且location中有"台"字
        if "台" in location:
          location = location.replace("台", "臺")

        # 若location在cityList中有出現
        # location = "".join(s for s in cityList if location in s)
        for s in range(len(cityList)):
          try:
            if location == cityList[s]:
            # Exact match
              location = cityList[s]
              # break

            if location in cityList[s]:
            # Partial match
              location = cityList[s]
              # break
            # else:
            #   print(location+"不在可搜尋範圍內。")
            #   break

            # if re.fullmatch(location,cityList[s]) == None:
            #   raise
            # print(cityList[s])

          except Exception:
            print(location+"不在可搜尋範圍內!!!!")
            break
              # pass

        # if re.fullmatch(location,cityList[s]) == None:
        #   print("想搜尋" + location[:2] + "市或" + location[:2] + "縣?")
        
        # for s in sililarCityList:
        #   # re.fullmatch(location,s) or 
        #   if location[:2].startswith(s[:2]):
        #     print("想搜尋" + s[:2] + "市或" + s[:2] + "縣?")

          # if any(location in s for s in sililarCityList):
          #   print("想搜尋" + location[:2] + "市或" + location[:2] + "縣?")
        url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization='
        response = requests.get(url + weather_api + '&locationName=' + location)

        # print(location.encode('utf-8').decode('unicode-escape'))
        # print(location.encode('ascii').decode('unicode-escape'))

        response.raise_for_status()
        if response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json"):
          data = response.json()
          dataDictList = []
          for place in data["records"]["location"]:  
            weatherDictList = []
            weatherEle = place['weatherElement']
            for w in weatherEle:
              timeDicts = w["time"]

              if w['elementName'] == "MinT":
              # 最低溫
                for timeDict in timeDicts:
                  weatherDictList.append({
                    "startTime": timeDict["startTime"],
                    "endTime": timeDict["endTime"],
                    "value": "最低溫 攝氏"+ timeDict['parameter']['parameterName']+"度" #+timeDict['parameter']['parameterUnit']
                  })
                  # print(timeDict["startTime"], timeDict["endTime"],timeDict['parameter']['parameterName']+timeDict['parameter']['parameterUnit'])

              if w['elementName'] == "MaxT":
                # 最高溫
                for timeDict in timeDicts:
                  weatherDictList.append({
                    "startTime": timeDict["startTime"],
                    "endTime": timeDict["endTime"],
                    "value": "最高溫 攝氏"+ timeDict['parameter']['parameterName']+"度"#+timeDict['parameter']['parameterUnit']
                  })
                  # print(timeDict["startTime"], timeDict["endTime"],timeDict['parameter']['parameterName']+timeDict['parameter']['parameterUnit'])

              if w['elementName'] == "Wx":
                # 天氣描述
                for timeDict in timeDicts:
                  weatherDictList.append({
                    "startTime": timeDict["startTime"],
                    "endTime": timeDict["endTime"],
                    "value": timeDict['parameter']['parameterName']
                  })
                  # print(timeDict["startTime"], timeDict["endTime"],timeDict['parameter']['parameterName'])
              if w['elementName'] == "PoP":
                # 降雨機率
                for timeDict in timeDicts:
                  weatherDictList.append({
                    "startTime": timeDict["startTime"],
                    "endTime": timeDict["endTime"],
                    "value": timeDict['parameter']['parameterName']+"%"
                  })
                  # print(timeDict["startTime"], timeDict["endTime"],timeDict['parameter']['parameterName'],timeDict['parameter']['parameterUnit'])
            tempDict = {
              "locationName": place["locationName"],
              "weatherDictList": weatherDictList
            } 
            dataDictList.append(tempDict) 
          print(dataDictList)
          return HttpResponse(location)
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
          # if i.message.text == "功能列表":
          #   # 回復「功能列表」按鈕樣板訊息
          #   line_bot_api.reply_message(i.reply_token,Featuresmodel().content())

          if i.message.text == "天氣":
            weatherResult = weatherAPI(i.message.text)
            # for key,value in weatherResult.items():
            #   # print(key,value)

            # line_bot_api.reply_message(i.reply_token,TextSendMessage(text=i.message.text))
            line_bot_api.reply_message(i.reply_token,TextSendMessage(text=weatherResult))

      return HttpResponse()
    else:
      return HttpResponseBadRequest()
