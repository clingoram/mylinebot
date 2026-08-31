from django.test import SimpleTestCase
from unittest.mock import mock_open, patch
from apps.stock.services import quotes # module

class StockNameFromJsonTest(SimpleTestCase):
    '''
    測cache行為：

    第一次呼叫_get_stock_name_from_json() → open()被呼叫一次
    第二次呼叫 → 使用現有cache，open()不應再次被呼叫。
    '''
    def setUp(self):
        # quotes.py中的_stock_name_cache，cache清空
        quotes._stock_name_cache = None

    def test__get_stock_name_load_json_only_once(self):
        '''
        兩次function call，json檔案應只被讀取一次。
        '''
        # 確保每個test開始時cache都是空的
        quotes._stock_name_cache = None

        mock_json_data = [
            {
                "公司代碼": "2330",
                "公司簡稱": "台積電",
            },
            {
                "公司代碼": "0050",
                "公司簡稱": "元大台灣50",
            },
        ]

        mock_file = mock_open()
        
        with patch("apps.stock.services.quotes.open",mock_file), patch(
           "apps.stock.services.quotes.json.load",
            return_value=mock_json_data,
        ):
            # 第一次呼叫：cache是None，應該讀JSON
            result1 = quotes._get_stock_name_from_json("2330")

            # 第二次呼叫：cache已存在，應該使用cache
            result2 = quotes._get_stock_name_from_json("0050")

        self.assertEqual(result1, "台積電")
        self.assertEqual(result2, "元大台灣50")

        # open只應該被呼叫一次
        mock_file.assert_called_once()