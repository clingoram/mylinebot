from django.conf import settings
from linebot import LineBotApi
import logging
logger = logging.getLogger(__name__)
LINE_BOT_API = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def reply(event_reply_token:str,message:str) -> None:
    '''
    line reply
    將LINE_BOT_API.reply_message() 做成公用涵式，只須call reply
    '''
    try:
        LINE_BOT_API.reply_message(event_reply_token,message)
    except Exception as e:
        # logging
        logger.exception(f"LINE reply error: {e}")