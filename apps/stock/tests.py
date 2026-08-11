from django.test import TestCase
from .models import HotStock,FavoriteStock
from linebot.models import TextSendMessage,TextMessage,FlexSendMessage
# class HotStockModelTest(TestCase):
#     def test_hotstock_can_insert(self):
#         stock = HotStock.objects.create(stock_id = '0050',stock_name = '元大台灣50',suffix = 'TWO')
#         stock.save()
#         self.assertTrue(stock)

    # def test_stock_has_exist(self):


# class FavoriteModelTest(TestCase):

# from unittest.mock import Mock, patch

# from django.test import TestCase
# from django.http import HttpResponse

# from apps.stock.services.handler import handle_stock_data


# class HandleStockDataTest(TestCase):

#     @patch("apps.stock.services.handler.get_stock_flex_message")
#     @patch("apps.stock.services.handler.LINE_BOT_API")
#     def test_handle_stock_data_success(self, mock_get_stock_flex_message,mock_line_bot,):
#         '''
#         有找到股票資料
#         '''
#         event = Mock()
#         event.message.text = "股票2330"
#         event.reply_token = "reply-token"

#         mock_get_stock_flex_message.return_value = {
#             "type": "bubble"
#         }

#         response = handle_stock_data(event)
#         mock_get_stock_flex_message.assert_called_once_with("2330")

#         # 注意這裡
#         mock_line_bot.reply_message.assert_called_once()

#         self.assertEqual(response.status_code, 200)

    # @patch("myapp.views.get_stock_flex_message")
    # @patch("myapp.views.LINE_BOT_API.reply_message")
    # def test_handle_stock_data_not_found(self,mock_reply_message,mock_get_stock_flex_message,):
    #     '''
    #     找不到股票資料
    #     '''
    #     event = Mock()
    #     event.message.text = "9999"
    #     event.reply_token = "reply-token"

    #     mock_get_stock_flex_message.return_value = None

    #     response = handle_stock_data(event)

    #     mock_get_stock_flex_message.assert_called_once_with("9999")

    #     mock_reply_message.assert_called_once()

    #     message = mock_reply_message.call_args.args[1]

    #     self.assertIsInstance(message, TextSendMessage)
    #     self.assertEqual(message.text, "請輸入股票代號")

    #     self.assertIsNone(response)


    # @patch("myapp.views.get_stock_flex_message")
    # @patch("myapp.views.LINE_BOT_API.reply_message")
    # def test_handle_stock_data_flex_message(self,mock_reply_message,mock_get_stock_flex_message,):
    #     '''
    #     FlexMessage
    #     '''
    #     event = Mock()
    #     event.message.text = "2330"
    #     event.reply_token = "reply-token"

    #     flex_data = {
    #         "type": "bubble",
    #         "body": {
    #             "type": "box"
    #         }
    #     }

    #     mock_get_stock_flex_message.return_value = flex_data

    #     response = handle_stock_data(event)

    #     message = mock_reply_message.call_args.args[1]

    #     self.assertIsInstance(message, FlexSendMessage)
    #     self.assertEqual(message.alt_text, "2330追蹤 2330")
    #     self.assertEqual(message.contents, flex_data)

    #     self.assertEqual(response.status_code, 200)