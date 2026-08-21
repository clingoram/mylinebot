from django.test import TestCase
from unittest.mock import Mock, patch,MagicMock
from apps.news.services.text_news import create_news_text
from apps.news.services.get_news import get_news
class TestNews(TestCase):
    '''
    測新聞
    '''

    # @patch("apps.news.services.handle_news")
    @patch("apps.news.services.get_news.requests.get")
    def test_get_news(self,mock_get):
        '''
        正常取得新聞
        mock requests.get()，但不要mock BeautifulSoup
        '''
        html = """
        <html>
        <body>
            <div class="news_list_item">
                <div class="title_pc">
                    <a href="/news.aspx?newsid=123">新聞標題一</a>
                </div>
                <div class="time_box">
                    <span class="tab">財經</span>
                    <span class="time">2026/08/21 10:00</span>
                </div>
            </div>

            <div class="news_list_item">
                <div class="title_pc">
                    <a href="/news.aspx?newsid=456">新聞標題二</a>
                </div>
                <div class="time_box">
                    <span class="tab">社會</span>
                    <span class="time">2026/08/21 11:00</span>
                </div>
            </div>
        </body>
    </html>
        """
        mock_response = MagicMock()
        mock_response.text = html
        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        result = get_news()

        self.assertEqual(len(result),2)
        self.assertEqual(result[0]["title"],"新聞標題一")
        self.assertEqual(result[0]["category"],"財經")
        self.assertEqual(result[0]["time"] , "2026/08/21 10:00")
        self.assertEqual(result[0]["source"] , "三立新聞網")
        self.assertEqual(result[0]["url"],"https://www.setn.com/news.aspx?newsid=123")

  