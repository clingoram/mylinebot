from django.conf import settings
from linebot import LineBotApi
LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def reply(event_reply_token,message:str) -> None:
    '''
    line reply
    將LINE_BOT_API.reply_message() 做成公用涵式，只須call reply
    '''
    try:
        LINE_BOT_API.reply_message(event_reply_token,message)
    except Exception as e:
        # logging
        print(f"LINE reply error: {e}")