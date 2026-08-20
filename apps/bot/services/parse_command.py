import re

def parse_command(text:str) -> dict:
    '''
    輸入解析
    '''
    text = text.strip()

    # =========================
    # 股票
    # 例如：
    # 股票2330
    # 股票 2330
    # =========================
    stock_match = re.fullmatch(r"股票\s*(\d{4,6})", text)

    if stock_match:
        return {
            "action": "stock",
            "stock_code": stock_match.group(1)
        }

    # 天氣
    if text.endswith(("市", "縣")):
        return {
            "action": "weather",
            "city": text
        }

    # =========================
    # 新聞
    #
    # 新聞
    # 新聞 台積電
    # 新聞 財經
    # 新聞 財經 台積電
    # =========================
    if text.startswith("新聞"):
        parts = text.split()
        parts = parts[1:]  # 移除「新聞」

        news_categories = {
            "政治",
            "財經",
            "社會",
            "娛樂",
            "體育",
            "科技",
            "生活",
            "國際"
        }

        category = None
        keyword = None

        if parts:
            # 第一個詞是新聞分類
            if parts[0] in news_categories:
                category = parts[0]
                parts = parts[1:]

            # 剩下的全部視為關鍵字
            if parts:
                keyword = " ".join(parts)

        return {
            "action": "news",
            "category": category,
            "keyword": keyword
        }

    if text in ["我的股票","追蹤清單"]:
        return {
            "action": "follow_list"
        }

    if text == "說明":
        return {
            "action" : "explain"
        }

    return {
        "action": "unknown",
        "text": text
    }