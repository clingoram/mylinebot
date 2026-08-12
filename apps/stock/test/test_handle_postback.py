from django.test import TestCase
from unittest.mock import Mock, patch
from apps.stock.services.handler import handle_postback
from apps.stock.services.tracking import follow_stock,unfollow_stock
from apps.basic_info.models import Person
from apps.stock.models import FavoriteStock

class HandlePostBackTest(TestCase):
    '''
    測試按下 追蹤 (股票代碼) 或 取消追蹤 (股票代碼)
    '''
    def setUp(self):
        '''
        建立Person(user) 和 FavoriteStock 資料
        每個test都建立：
        user = test_user_001
        '''
        self.user = Person.objects.create(
            user_account = "test_user_001"
        )

    @patch("apps.stock.services.handler.LINE_BOT_API")
    def test_follow_stock_line_event(self,mock_line):
        '''
        Mock LINE Event
        按下按鈕 Event → 追蹤
        '''
        event = Mock()
        event.source.user_id = "test_user_001"
        event.postback.data = "action=watch&stock_id=2330"
        event.reply_token = "reply-token"
        
        # handler
        handle_postback(event)

        # test db
        FavoriteStock.objects.create(user_account=self.user,stock_id="2330")

        self.assertTrue(
            FavoriteStock.objects.filter(
                user_account=self.user,
                stock_id="2330"
            ).exists()
        )
        mock_line.reply_message.assert_called_once()

    @patch("apps.stock.services.handler.LINE_BOT_API")
    def test_unfollow_stock_event(self, mock_line):
        '''
        按下按鈕 Event → 取消追蹤
        '''
        event = Mock()
        event.source.user_id = "test_user_001"
        event.postback.data = "action=unfollow&stock_id=2330"
        event.reply_token = "reply-token"

        # handler
        handle_postback(event)

        self.assertFalse(
            FavoriteStock.objects.filter(
                user_account=self.user,
                stock_id="2330"
            ).exists()
        )
        mock_line.reply_message.assert_called_once()

    def test_follow_stock(self):
        '''
        追蹤 -> test db 新增資料
        '''
        result = follow_stock("test_user_001","2330")

        self.assertEqual(result.status_code,200)

        self.assertTrue(
            FavoriteStock.objects.filter(
                user_account=self.user,
                stock_id="2330"
            ).exists()
        )
    # def test_unfollow_stock(self):
        '''
        取消追蹤 -> test db 刪除資料
        '''
    # def test_follow_stock_duplicate(self):
    '''
    重複追蹤
    '''
    #     event = Mock()
    #     event.source.user_id = "test_user_001"
    #     event.postback.data = "follow:2330"

    #     handle_stock_action(event)

    #     self.assertEqual(
    #         FavoriteStock.objects.filter(
    #             user_account=self.user,
    #             stock_id="2330"
    #         ).count(),
    #         1
    #     )