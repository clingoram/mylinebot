from django.test import TestCase
from unittest.mock import patch
from apps.bot.services.line_reply import reply

class LineReplyTest(TestCase):
    @patch("apps.bot.services.line_reply.LINE_BOT_API.reply_message")
    def test_line_reply(self,mock_bot_reply):
        '''
        測試reply_token
        確認LINE webhook傳進來的token有正確傳給reply()
        '''
        message = "Call LINE"
        reply("token", message)

        mock_bot_reply.assert_called_once_with("token",message)