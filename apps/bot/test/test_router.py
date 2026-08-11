from django.test import TestCase
from unittest.mock import Mock, patch
from apps.bot.router import route_event

class RouterTest(TestCase):
    '''
    測分流
    '''
    # 暫時把真的XXXX()換掉，避免測試真的執行它，由下往上對應
    @patch("apps.bot.router.handle_stock_data") # mock stock
    @patch("apps.bot.router.create_Keyword") # mock key word
    @patch("apps.bot.router.create_user") # mock create user
    @patch("apps.bot.router.Person.objects.filter") # mock Person.objects.filter
    def test_route_stock(self,mock_filter,mock_create_user,mock_create_keyword,mock_stock,):
        event = Mock() # 假的東西，讓測試時不用真的執行某些功能，假裝LINE傳進來的Event

        event.type = "message"
        event.message.type = "text"
        event.message.text = "股票2330"
        event.source.user_id = "test_user_001"

        # 模擬使用者已存在
        mock_filter.return_value.exists.return_value = True

        route_event([event])

        mock_create_keyword.assert_called_once_with("test_user_001","股票2330",)

        mock_stock.assert_called_once_with(event)
        mock_create_user.assert_not_called()


    @patch("apps.bot.router.create_Keyword")
    @patch("apps.bot.router.Person.objects.filter")
    @patch("apps.bot.router.handle_weather")
    def test_route_weather(self, mock_weather,mock_filter,mock_create_keyword):
        '''
        天氣
        '''
        event = Mock()
        event.type = "message"
        event.message.type = "text"
        event.message.text = "高雄市"
        event.source.user_id = "test_user_001"

        route_event([event])

        # 模擬使用者已存在
        mock_filter.return_value.exists.return_value = True

        mock_weather.assert_called_once_with(event)
        mock_create_keyword.assert_called_once_with("test_user_001","高雄市",)


    @patch("apps.bot.router.handle_news")
    @patch("apps.bot.router.create_user")
    @patch("apps.bot.router.create_Keyword")
    @patch("apps.bot.router.Person.objects.filter")
    def test_route_news(self,mock_filter,mock_create_keyword,mock_create_user,mock_news,):
        '''
        爬蟲
        '''
        event = Mock()
        event.type = "message"
        event.message.type = "text"
        event.message.text = "新聞"
        event.source.user_id = "test_user_001"

        route_event([event])

        mock_filter.return_value.exists.return_value = True
        mock_news.assert_called_once_with(event)
        mock_create_keyword.assert_called_once_with("test_user_001","新聞",)
        mock_create_user.assert_not_called()