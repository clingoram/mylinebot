import yfinance as yf


# 負責call API拿原始英文資料（內部私有）
def _fetch_api_data(stock_number:str):
    '''

    取得https://github.com/ranaroussi/yfinance 資料
    但這資料是英文，部份須轉換成中文

    '''
    stock = yf.Ticker(stock_number+".TW") # yfinance 台股代號後面須加上.TW，例如：1234.TW
    # print(yf.__version__)
    # stock 代碼可能不存在 => 打錯數字之類的
    df = stock.history(period="1d",auto_adjust=False)
    # print(df.columns)
    if df.empty:
        return "查無該股票存在"
    
    info = stock.info
    # print(info.get("longName"))
    if not info:
       return "查無該股票存在"

    # print(json.dumps(info, indent=4, ensure_ascii=False))
    # print(df['Close'].values)
    return _map_eng_to_chinese(info,df)

def _map_eng_to_chinese(info:dict,df):
    '''
    負責mapping 成中文資料（內部私有）

    mapping 原始資料（英文）資訊至中文
    '''
    
    announce = "⚠️ 此line bot之股票資料是從API取得。只提供股票相關資訊且用於個人side-project，不具有任何投資理財目的。 ⚠️"
    content = ""
    fieldMap = {
        "代碼":info.get("symbol").strip(".TW"),
        "公司名稱":info.get("longName"),
        "產業":info.get("sector"),
        "類型":typeDisp(info.get("typeDisp")),

        "開盤價":info.get("open"),
        "即時價格":info.get("currentPrice"),
        "昨收":info.get("regularMarketPreviousClose"),

        "當日最低":info.get("dayLow"),
        "當日最高":info.get("dayHigh"),
        "收盤價":",".join(map(str, df["Close"])), # df["Close"].tolist(),
        # "調整後收盤價":df["Adj Close"].tolist(),

        "市值":fmt_num(info.get("marketCap")), # 只加千分位，不保留小數
        "本益比":fmt_num(info.get("trailingPE")),
        "預估本益比":info.get("forwardPE"),

        "殖利率":info.get("dividendYield"),
        "年配息":info.get("dividendRate"),
        "52週高": info.get("fiftyTwoWeekHigh"),
        "52週低": info.get("fiftyTwoWeekLow"),
    }
    # for key,value in info.items():
    #     if key in fieldMap:
    #       content += f"{fieldMap[key]}: {value}\n"

    # for key,value in fieldMap.items():
    #     content+= f"{key}: {value}\n"
    # return f"{announce} \n" + "\n"+ content

    return fieldMap

def typeDisp(infoType:str):
    '''
    股票類型
    '''
    stockType = {
        "Equity":"普通股票",
        "ETF":"指數型基金",
        "Index":"指數",
        "Cryptocurrency":"加密貨幣",
        "Future":"期貨",
        "Currency":"外匯"
    }
    for key,value in stockType.items():
        if infoType == key:
            return value
    return "無資料"

def fmt_num(value):
    '''
    若None顯示N/A
    '''
    # return f"{v:,.0f}" if isinstance(v, (int, float)) else "N/A"
    if value is None:
        return "N/A"
    return f"{value:,.0f}"


# ❌
def get_stock_realtime_data(stock_code):
    """
    吐出純中文Dict資料。
    這是專門支援tracking.py，讓它去打包「自選股清單 Flex」用的
    """
    raw_data = _fetch_api_data(stock_code)
    if not raw_data:
        return None
        
    chinese_data = _map_eng_to_chinese(raw_data)
    
    # 補上代碼，讓外面的 tracking.py 好處理
    chinese_data["code"] = stock_code 
    
    return chinese_data 
    # 最終回傳一個乾淨的中文資料 Dict，例如：
    # {"code": "2330", "name": "台積電", "price": 1005, "change_percent": "+1.5", "trend": "up"}
    
# ❌
def get_stock_flex_message(key):
    '''
    flex message

    主要對外接口，給router.py 用於「單檔股票查詢」的，整合_fetch_api_data() & _map_eng_to_chinese() 並建立Flex Message

    串聯：Call API -> 轉中文 -> 塞入Flex Message
    '''
    stockO = _fetch_api_data(key)

    contents = []

    for key, value in stockO.items():
        contents.append({
            "type": "box",
            "layout": "baseline",
            "contents": [
                {
                    "type": "text",
                    "text": key,
                    "size": "sm",
                    "color": "#888888",
                    "flex": 2
                },
                {
                    "type": "text",
                    "text": str(value),
                    "size": "sm",
                    "align": "end",
                    "flex": 3
                }
            ]
        })

    bubble = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": stockO["代碼"].strip(".TW"),
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "separator",
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": contents
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "action": {
                        "type": "postback",
                        "label": "加入追蹤",
                        "data": f"action=watch&stock_id={stockO['代碼']}"
                    }
                }
            ]
        }
    }
    return bubble