from django.test import TestCase
from unittest.mock import Mock, patch
from apps.stock.services.handler import handle_followlist
from apps.stock.services.tracking import get_user_stocks_list,_get_hot_stocks_by_ids,_batch_processing_multiple_stocks


from apps.basic_info.models import Person
from apps.stock.models import FavoriteStock,HotStock

class HandleFollowStockListTest(TestCase):
    '''
    股票清單
    分成有追蹤有資料和沒有追蹤沒資料的test case
    '''
    def setUp(self):
        '''
        準備測試用DB資料
        建立Person(user)、FavoriteStock和HotStock資料
        '''
        self.user = Person.objects.create(
            user_account = "test_user_001"
        )

        self.stock1 = FavoriteStock.objects.create(
            user_account=self.user,
            stock_id="2330"
        )

        self.stock2 = FavoriteStock.objects.create(
            user_account=self.user,
            stock_id="0050"
        )

        self.stock3 = FavoriteStock.objects.create(
            user_account=self.user,
            stock_id="2034"
        )

        self.hstock1 = HotStock.objects.create(
            stock_id = "2330",
            stock_name = "台積電",
            suffix = "TW"
        )
        self.hstock2 = HotStock.objects.create(
            stock_id = "0050",
            stock_name = "元大台灣50",
            suffix = "TW"
        )
        self.hstock3 = HotStock.objects.create(
            stock_id = "2034",
            stock_name = "允強",
            suffix = "TW"
        )

    @patch("apps.stock.services.tracking._fetch_api_data")
    @patch("apps.stock.services.tracking._get_hot_stocks_by_ids")
    def test_batch_processing_multiple_stocks(self,mock_hot_stock_from_db,mock_fetch_api_data):
        '''
        stock ID是否正確clean
        mock_hot_stock_from_db()是否收到正確的id
        _fetch_api_data() 是否逐一被呼叫
        API回傳None時是否不加入結果
        API有資料時是否正確組成list
        '''
        mock_hot_stock_from_db.return_value = {}

        mock_fetch_api_data.side_effect = [
            {
                "代碼": "2330",
                "公司名稱": "台積電",
                "即時價格": 2300,
            },
            {
                "代碼": "0050",
                "公司名稱": "元大台灣50",
                "即時價格": 82,
            },
        ]

        result = _batch_processing_multiple_stocks(["2330", "0050"])

        mock_hot_stock_from_db.assert_called_once_with(["2330", "0050"])

        self.assertEqual(mock_fetch_api_data.call_count,2)

        self.assertEqual(len(result),2)

    def test_get_hot_stocks_by_ids(self):
        '''
        給定stock_id，應從DB找出對應的HotStock並以stock_id作為dict key
        '''
        result = _get_hot_stocks_by_ids(stock_id= ["2330","0050","2034"])

        self.assertEqual(len(result),3)
        self.assertEqual(set(result.keys()),{"2330", "0050", "2034"})

    def test_get_hot_stocks_by_ids_returns_existing_stocks_only(self):
        '''
        傳入不存在的stock_id，不應該產生資料
        '''

        result = _get_hot_stocks_by_ids(stock_id= ["2330","0050","9999"])

        self.assertEqual(len(result), 2)
        self.assertEqual(set(result.keys()),{"2330", "0050"})

    @patch("apps.stock.services.tracking._batch_processing_multiple_stocks")
    def test_get_user_stocks_list_has_data(self, mock_batch_stocks):
        """
        DB有資料 → 正確取得股票清單 → 批次處理給_batch_processing_multiple_stocks
        """
        mock_batch_stocks.return_value = [
            {
                "代碼": "2330",
                "公司名稱": "台積電",
                "即時價格": 2300,
            },
            {
                "代碼": "0050",
                "公司名稱": "元大台灣50",
                "即時價格": 82,
            },
            {
                "代碼": "2034",
                "公司名稱": "允強",
                "即時價格": 20.45,
            },
]

        get_user_stocks_list(user_id=self.user.user_account)

        mock_batch_stocks.assert_called_once_with(stock_id=["2330", "0050","2034"])

    @patch("apps.stock.services.tracking._fetch_api_data")
    def test_get_user_stocks_list_no_data(self,mock_fetch_api_data):
        '''
        DB沒有資料->空清單的Flex Message是否正確
        '''
        FavoriteStock.objects.filter(user_account=self.user).delete()

        result = get_user_stocks_list(user_id=self.user.user_account)

        self.assertEqual(result["type"],"carousel")
    
        mock_fetch_api_data.assert_not_called()


    @patch("apps.stock.services.handler.reply")
    @patch("apps.stock.services.tracking._fetch_api_data")
    def test_handle_stock_has_follow_list(self,mock_sotck_fetch_api,mock_reply):
        '''
        mock event → 查到有資料 → LINE reply是否正常
        '''
        event = Mock()
        event.source.user_id = "test_user_001"
        event.reply_token = "reply-token"

        result = handle_followlist(event=event)

        self.assertEqual(result,None)
  
        mock_sotck_fetch_api.side_effect = [
            {
                "代碼": "2330",
                "公司名稱": "台積電",
                "即時價格":2420
            },
            {
                "代碼": "0050",
                "公司名稱": "元大台灣50",
                "即時價格":106
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

        result = handle_followlist(event=event)

        self.assertEqual(result,None)
        # 有沒有叫reply()
        mock_reply.assert_called_once()
