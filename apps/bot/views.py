from apps.bot.router import route_event
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot.exceptions import InvalidSignatureError, LineBotApiError,BaseError
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from linebot.webhook import WebhookParser
LINE_WEBHOOK_PARSER = WebhookParser(settings.LINE_CHANNEL_SECRET)

import logging
logger = logging.getLogger(__name__)


@csrf_exempt
def handle_message(request):
  if request.method != 'POST':
    return HttpResponse("Method not allowed", status=405)
    
  # print("👉 收到LINE callback 👈")
  logger.info("👉 收到LINE callback 👈")

  body = request.body.decode('utf-8')
  signature = request.META.get("HTTP_X_LINE_SIGNATURE")

  if not signature:
    return HttpResponseBadRequest("Missing X-Line-Signature")

  try:
    # 傳入事件
    handleEvent = LINE_WEBHOOK_PARSER.parse(body, signature)
  except InvalidSignatureError:
    return HttpResponseForbidden()
  except LineBotApiError:
    return HttpResponseBadRequest()
  except BaseError:
    return HttpResponse("發生錯誤", status=400)
  
  return route_event(handleEvent)