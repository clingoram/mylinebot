from apps.crawler.services.crawler import crawler_news

def create_news_flex(news_list):
    '''
    將從beautifulsoup取得的新聞塞進flex message內
    '''
    call_news = crawler_news()