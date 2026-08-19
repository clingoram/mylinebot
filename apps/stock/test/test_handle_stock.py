from django.test import SimpleTestCase
from unittest.mock import Mock, patch
from apps.stock.services.handler import handle_stock_data
from linebot.models import TextSendMessage,FlexSendMessage
class HandleStockTest(SimpleTestCase):
    '''
    查詢單一股票
    不會真的call API，用Mock和@patch
    '''
    @patch("apps.stock.services.handler.reply")
    @patch("apps.stock.services.handler.get_stock_flex_message")
    def test_handle_stock_data(self,mock_get_stock,mock_reply):
        '''
        有資料
        '''
        event = Mock()
        event.message.text = "2330"
        event.reply_token = "reply-token"

        mock_get_stock.return_value = {
            "type": "bubble"
        }

        response = handle_stock_data(event)

        mock_get_stock.assert_called_once_with("2330")

        # 有沒有叫reply()
        mock_reply.assert_called_once()

        self.assertEqual(response, None)
        # 檢查送的是FlexSendMessage，而不是TextSendMessage
        args = mock_reply.call_args
        self.assertEqual(args[0][0],"reply-token")
        self.assertIsInstance(args[0][1],FlexSendMessage)

    @patch("apps.stock.services.handler.reply")
    @patch("apps.stock.services.handler.get_stock_flex_message")
    def test_handle_stock_no_data(self,mock_get_stock,mock_reply):
        '''
        股票代碼亂輸入->無資料
        '''
        event = Mock()
        event.message.text = "Today"
        event.reply_token = "reply-token"

        mock_get_stock.return_value = {
            "type": "bubble"
        }

        response = handle_stock_data(event)

        mock_get_stock.assert_called_once_with("Today")

        # 有沒有叫reply()
        mock_reply.assert_called_once()

        self.assertEqual(response, None)
        # 檢查送的是TextSendMessage，而不是FlexSendMessage
        args = mock_reply.call_args
        self.assertEqual(args[0][0],"reply-token")
        self.assertNotIsInstance(args[0][1],TextSendMessage)