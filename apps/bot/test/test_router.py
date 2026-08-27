from django.test import TestCase,SimpleTestCase
from unittest.mock import Mock, patch
from apps.bot.router import route_event

class RouterTest(SimpleTestCase):
    '''
    測分流
    '''
    @patch("apps.bot.router.handle_stock_data") # mock stock
    @patch("apps.bot.router.create_Keyword") # mock key word
    @patch("apps.bot.router.create_user") # mock create user
    @patch("apps.bot.router.Person.objects.filter") # mock Person.objects.filter
    def test_route_stock(self,mock_filter,mock_create_user,mock_create_keyword,mock_stock,):
        '''
        測股票分流
        '''
        event = Mock()
        event.type = "message"
        event.message.type = "text"
        event.message.text = "股票2330"
        event.source.user_id = "test_user_001"

        # 模擬使用者已存在
        mock_filter.return_value.exists.return_value = True

        route_event([event])

        mock_create_keyword.assert_called_once_with(user_id = "test_user_001",keyword = "股票2330",)
        mock_stock.assert_called_once_with(event = event,stock_id = "2330")
        mock_create_user.assert_not_called()


    @patch("apps.bot.router.create_Keyword")
    @patch("apps.bot.router.Person.objects.filter")
    @patch("apps.bot.router.handle_weather")
    def test_route_weather(self, mock_weather,mock_filter,mock_create_keyword):
        '''
        測天氣分流
        '''
        event = Mock()
        event.type = "message"
        event.message.type = "text"
        event.message.text = "高雄市"
        event.source.user_id = "test_user_001"

        # 模擬使用者已存在
        mock_filter.return_value.exists.return_value = True

        route_event([event])

        mock_weather.assert_called_once_with(event=event,location = "高雄市")
        mock_create_keyword.assert_called_once_with(user_id = "test_user_001",keyword = "高雄市",)


    @patch("apps.bot.router.handle_news")
    @patch("apps.bot.router.create_user")
    @patch("apps.bot.router.create_Keyword")
    @patch("apps.bot.router.Person.objects.filter")
    def test_route_news(self,mock_filter,mock_create_keyword,mock_create_user,mock_news,):
        '''
        測新聞分流
        '''
        event = Mock()
        event.type = "message"
        event.message.type = "text"
        event.message.text = "新聞"
        event.source.user_id = "test_user_001"

        mock_filter.return_value.exists.return_value = True
        route_event([event])

        mock_news.assert_called_once_with(event = event,keyword = None,category = None)
        mock_create_keyword.assert_called_once_with(user_id = "test_user_001",keyword = "新聞")
        mock_create_user.assert_not_called()

    @patch("apps.bot.router.explain")
    @patch("apps.bot.router.create_Keyword")
    @patch("apps.bot.router.Person.objects.filter")
    def test_route_explain(self,mock_filter,mock_create_keyword,mock_explain):
        '''
        測說明分流
        '''
        event = Mock()
        event.type = "message"
        event.message.type = "text"
        event.message.text = "說明"
        event.source.user_id = "test_user_001"

        # 模擬使用者已存在
        mock_filter.return_value.exists.return_value = True
        
        route_event([event])
        mock_explain.assert_called_once_with(event = event)
        mock_create_keyword.assert_called_once_with(user_id = "test_user_001",keyword = "說明")