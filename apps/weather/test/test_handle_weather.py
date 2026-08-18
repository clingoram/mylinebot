from django.test import TestCase
from unittest.mock import Mock, patch
from apps.weather.services.handle_weather import handle_weather,flex_message
from linebot.models import TextSendMessage,FlexSendMessage

class HandleWeatherTest(TestCase):
    '''
    查詢天氣
    LINE收到訊息後，整個處理流程對不對
    不是真的call API
    '''
    @patch("apps.weather.services.handle_weather.reply")
    @patch("apps.weather.services.handle_weather.flex_message")
    def test_handle_weather_has_the_city(self,mock_flex,mock_reply):
        '''
        測試event.message.text
        有資料->FlexSendMessage
        '''
        event = Mock()
        event.message.text = "高雄市"
        event.reply_token = "reply-token"

        mock_flex.return_value = {
            "type": "bubble"
        }

        handle_weather(event)
        mock_flex.assert_called_once_with("高雄市")
        mock_reply.assert_called_once()
        # 檢查送的是FlexSendMessage，而不是TextSendMessage
        args = mock_reply.call_args
        self.assertEqual(args[0][0],"reply-token")
        self.assertIsInstance(args[0][1],FlexSendMessage)

    @patch("apps.weather.services.handle_weather.reply")
    @patch("apps.weather.services.handle_weather.flex_message")
    def test_handle_weather_hasnot_the_city(self,mock_flex,mock_reply):
        '''
        測試event.message.text
        沒資料->TextSendMessag
        '''
        event = Mock()
        event.message.text = "小琉球"
        event.reply_token = "reply-token"

        mock_flex.return_value = {}

        handle_weather(event)
        mock_reply.assert_called_once()
        # 檢查送的是TextSendMessage，而不是FlexSendMessage
        args = mock_reply.call_args
        self.assertEqual(args[0][0],"reply-token")
        self.assertIsInstance(args[0][1],TextSendMessage)

    