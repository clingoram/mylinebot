from django.test import TestCase
from unittest.mock import Mock, patch
from apps.stock.services.handler import handle_followlist
from apps.stock.services.tracking import get_user_stocks_list


from apps.basic_info.models import Person
from apps.stock.models import FavoriteStock

class HandleFollowStockListTest(TestCase):
    '''
    股票清單
    分成有追蹤有資料和沒有追蹤沒資料的test case
    '''
    def setUp(self):
        '''
        建立Person(user) 和 FavoriteStock 資料
        每個test都建立：
        user = test_user_001
        FavoriteStock = 2330
        FavoriteStock = 0050
        '''
        self.user = Person.objects.create(
            user_account = "test_user_001"
        )

        FavoriteStock.objects.create(
            user_account=self.user,
            stock_id="2330"
        )

        FavoriteStock.objects.create(
            user_account=self.user,
            stock_id="0050"
        )

    @patch("apps.stock.services.tracking._fetch_api_data")
    def test_get_user_stocks_list_has_data(self,mock_fetch_api_data,):
        '''
        DB有資料 → Flex Message是否正確
        '''
        mock_fetch_api_data.side_effect = [
            {
                "代碼": "2330","公司名稱": "台積電","即時價格":2300
            },
            {
                "代碼": "0050","公司名稱": "元大台灣50","即時價格":82
            },
        ]

        result = get_user_stocks_list(self.user.user_account)

        mock_fetch_api_data.assert_any_call("2330")
        mock_fetch_api_data.assert_any_call("0050")

        self.assertEqual(mock_fetch_api_data.call_count,2)

    @patch("apps.stock.services.tracking._fetch_api_data")
    def test_get_user_stocks_list_no_data(self,mock_fetch_api_data,):
        '''
        DB沒有資料->空清單的Flex Message是否正確
        '''
        FavoriteStock.objects.filter(user_account=self.user).delete()

        result = get_user_stocks_list(self.user.user_account)

        self.assertEqual(result["type"],"carousel")
    
        mock_fetch_api_data.assert_not_called()


    @patch("apps.stock.services.handler.reply")
    @patch("apps.stock.services.tracking._fetch_api_data")
    def test_handle_stock_has_follow_list(self,mock_sotck_fetch_api,mock_reply,):
        '''
        mock event → 查到有資料 → LINE reply是否正常
        '''
        event = Mock()
        event.source.user_id = "test_user_001"
        event.reply_token = "reply-token"

        result = handle_followlist(event)

        self.assertEqual(result,None)
  
        mock_sotck_fetch_api.side_effect = [
            {
                "代碼": "2330","公司名稱": "台積電","即時價格":2000
            },
            {
                "代碼": "0050","公司名稱": "元大台灣50","即時價格":1999
            },
        ]

        # 有沒有叫reply()
        mock_reply.assert_called_once()


    @patch("apps.stock.services.handler.reply")
    def test_handle_stock_hasnot_follow_list(self,mock_reply):
        '''
        mock event → 沒資料 → LINE reply是否正常
        '''
        # 由於是沒有追蹤股票，因此把預先建立的這個user的測試資料刪除
        FavoriteStock.objects.filter(user_account=self.user.delete())

        event = Mock()
        event.source.user_id = "test_user_001"
        event.reply_token = "reply-token"

        result = handle_followlist(event)

        self.assertEqual(result,None)
        # 有沒有叫reply()
        mock_reply.assert_called_once()
