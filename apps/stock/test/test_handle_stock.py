from django.test import SimpleTestCase
from unittest.mock import Mock, patch
from apps.stock.services.handler import handle_stock_data

class HandleStockTest(SimpleTestCase):
    '''
    查詢單一股票
    不會真的call API，用Mock和@patch
    '''
    @patch("apps.stock.services.handler.LINE_BOT_API")
    @patch("apps.stock.services.handler.get_stock_flex_message")
    def test_handle_stock_data(self,mock_get_stock,mock_line_bot,):
        event = Mock()
        event.message.text = "股票2330"
        event.reply_token = "reply-token"

        mock_get_stock.return_value = {
            "type": "bubble"
        }

        response = handle_stock_data(event)

        mock_get_stock.assert_called_once_with("2330")

        mock_line_bot.reply_message.assert_called_once()

        self.assertEqual(response.status_code, 200)