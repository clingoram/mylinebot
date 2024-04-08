from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

# line bot
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# Create your views here.
@csrf_exempt
def callbackLine(request):
    '''
    line bot
    '''
    if request.method == 'POST':
      signature = request.META['HTTP_X_LINE_SIGNATURE']
      body = request.body.decode('utf-8')

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

def weatherAPI(request):
    '''
    氣象局API
    '''
    if request.method == "GET":  
      response = requests.get('api') #
      data = response.json()
      print(data)
      return HttpResponse("Users")
    pass