from django.test import SimpleTestCase
from unittest.mock import Mock
from apps.bot.services.parse_command import parse_command

class ParseCMDTest(SimpleTestCase):
    '''
    輸入解析測試
    測在line聊天室輸入的開頭分流關鍵字，例如：股票、新聞
    '''

    def test_to_the_router_keyword(self):
        '''
        測試分流關鍵字回傳的資料格式
        '''
        mock = Mock()
        mock.text = "新聞".strip()

        result = parse_command(text = mock.text)
        self.assertEqual(result["action"],"news")
        self.assertIsInstance(result,dict)
