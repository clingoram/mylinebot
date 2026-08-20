import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawler_news(keyword=None, category=None, limit=10):
    '''
    SETN 新聞爬蟲

    keyword  : 搜尋新聞標題關鍵字
    category : 新聞類型，例如「財經」、「社會」
    limit    : 最多取得幾筆
    '''
    # 由於SETN新聞存在HTML上，所以使用BeautifulSoup
    URL = "https://www.setn.com/viewall"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            "AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome/139.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(
        URL,
        headers=headers,
        timeout=10
    )
    response.raise_for_status()
    # docs: https://beautiful-soup-4.readthedocs.io/en/latest/#
    soup = BeautifulSoup(response.text, 'html.parser')
    content_list = []
    elements = soup.select(".news_list_item")

    for i in elements:
        # 新聞標題
        title_element = i.select_one(".title_pc a")

        # 新聞類型
        category_element = i.select_one(".time_box .tab")

        # 發布時間
        time_element = i.select_one(".time_box .time")

        if not title_element:
            continue

        title = title_element.get_text(strip = True)

        # href不一定是完整URL，所以用urljoin()
        news_url = urljoin(URL,title_element.get("href", ""))

        # 分類
        news_category = (
            category_element.get_text(strip = True)
            if category_element else ""
        )

        news_time = (
            time_element.get_text(strip = True)
            if time_element else ""
        )

        # 關鍵字篩選
        if keyword and keyword not in title:
            continue

        # 類別篩選
        if category and category != news_category:
            continue

        content_list.append({
            "title": title,
            "category": news_category,
            "time": news_time,
            "source":"三立新聞網",
            "url": news_url
        })

        if len(content_list) >= limit:
            break

    return content_list

