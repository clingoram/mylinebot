from django.conf import settings
from apps.weather.services.flexMsg import flex_message
from apps.bot.services.line_reply import reply
from cityList import city
from linebot.models import TextSendMessage,FlexSendMessage


def handle_weather(event,location):
    '''
    將得到的氣象資料塞進line bot內
    '''
    result = flex_message(location=location)
    if result:
        reply(event.reply_token,FlexSendMessage(alt_text = location + "氣象資訊",contents=result))
    else:
        reply(event.reply_token,TextSendMessage(text = location + "不在可搜尋範圍內。可搜尋: "+",".join(city())))
            