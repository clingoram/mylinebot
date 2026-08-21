from apps.news.services.get_news import get_news

def create_news_text(keyword=None, category=None):
    '''
    將從beautifulsoup取得的新聞塞進text message內
    '''
    call_news = get_news(keyword, category,5)

    if not call_news:
        return "找不到符合條件的新聞。"

    messages = []

    for i, news in enumerate(call_news, 1):
        messages.append(
            f"{i}. {news['title']}\n"
            f"類別：{news['category']}\n"
            f"來源：{news['source']}\n"
            f"時間：{news['time']}\n"
            f"原文：{news['url']}"
        )

    return "\n\n".join(messages)