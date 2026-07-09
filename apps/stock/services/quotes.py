import yfinance as yf
from apps.stock.models import HotStock
# ❌
# 負責call API拿原始英文資料（內部私有）
def _fetch_api_data(stock_number:str):
    '''

    取得https://github.com/ranaroussi/yfinance 資料
    但這資料是英文，部份須轉換成中文

    '''
    # find = ""
    # symbol =""
    # if stock_number.isdigit():
    #     find = HotStock.objects.filter(stock_id=stock_number).first()
    # else:
    #     find = HotStock.objects.filter(stock_name=stock_number).first()
    
    # 先從table找對應資料
    # yfinance 台股代號後面須加上.TW或.TWO，例如：1234.TW
    find = HotStock.objects.filter(stock_id = stock_number).first()
    if find:
        symbol = f"{find.stock_id}.{find.suffix}"
        stock_name = find.stock_name
    else:
        # 查無此股票
        return "查無該股票存在"
    
    stock = yf.Ticker(symbol)
    # print(yf.__version__)
    df = stock.history(period="1d",auto_adjust=False)

    # print(df.columns)
    # if df.empty:
    #     return "查無該股票存在"
    
    info = stock.info

    return _map_eng_to_chinese(info,df)
    # return _get_stock_change(info,df)

def _get_stock_change(data:dict):
    # 讀取API的漲跌欄位
    change = data.get('regularMarketChange')
    change_percent = data.get('regularMarketChangePercent')
    
    # 如果欄位不存在，啟動人工計算
    if change is None or change_percent is None:
        # 取得當前價格（防呆機制）
        current_price = data.get('currentPrice') or data.get('regularMarketPrice')
        previous_close = data.get('previousClose')
        
        if current_price and previous_close:
            change = current_price - previous_close
            # 計算百分比並四捨五入到小數點後兩位
            change_percent = (change / previous_close) * 100
            
    return {
        'change': round(change, 2) if change else 0.0,
        'change_percent': round(change_percent, 2) if change_percent else 0.0
    }

def _map_eng_to_chinese(info:dict,df):
    '''
    負責mapping 成中文資料（內部私有）

    mapping 原始資料（英文）資訊至中文
    '''
    
    # announce = "⚠️ 此line bot之股票資料是從API取得。只提供股票相關資訊且用於個人side-project，不具有任何投資理財目的。 ⚠️"
    # content = ""
    change =_get_stock_change(info)

    fieldMap = {
        "代碼":info.get("symbol").strip(".TW"),
        "公司名稱":info.get("longName"),
        "產業":info.get("sector"),
        "類型":typeDisp(info.get("typeDisp")),

        # "開盤價":info.get("open"),
        "即時價格":info.get("currentPrice"),
        "昨收":info.get("regularMarketPreviousClose"),

        "當日最低":info.get("dayLow"),
        "當日最高":info.get("dayHigh"),
        "收盤價":",".join(map(str, df["Close"])), # df["Close"].tolist(),
        # "調整後收盤價":df["Adj Close"].tolist(),
        "漲跌":change.get("change_percent"),

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

def get_stock_flex_message(key):
    '''
    flex message (單一股票)

    主要對外接口，給router.py用於「單檔股票查詢」

    串聯：Call API(_fetch_api_data()) -> 轉中文(_map_eng_to_chinese()) -> 塞入這個Flex Message
    '''
    stockO = _fetch_api_data(key)

    contents = []

    if len(stockO) > 0:
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
    else:
        return "無資料"