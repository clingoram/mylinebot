def translate(info):
    '''
    mapping部份英文資訊至中文
    '''
    announce = "⚠️ 此line bot之股票資料是從API取得。只提供股票相關資訊且用於個人side-project，不具有任何投資理財目的。 ⚠️"
    content = ""
    # fieldMap = {
    #     # "city":"公司總部",
    #     "longName": "公司名稱",
    #     "sector": "產業",
    #     # "industry": "子產業",
    #     # "symbol":"股票代碼",
    #     # 股價相關
    #     "Open": "開盤價",
    #     "currentPrice":"即時價格",
    #     "previousClose":"昨收",
    #     # "High": "最高價",
    #     # "Low": "最低價",
    #     "dayLow":"當日最低",
    #     "dayHigh":"當日最高",
    #     "Close": "收盤價",
    #     "Adj Close": "調整收盤價",
    #     # 交易量與流動性
    #     # "Volume": "成交量",
    #     # "Payout Ratio":"配息率",
    #     "marketCap": "市值",
    #     "trailingPE": "本益比",
    #     "forwardPE": "預估本益比",
    #     "dividendYield": "殖利率",
    #     "dividendRate":"年配息",
    #     "52週高": info.get("fiftyTwoWeekHigh"),
    #     "52週低": info.get("fiftyTwoWeekLow"),
    #     # "priceToBook":"股價淨值比",
    #     # "pegRatio":"成長估值",
    #     # "totalRevenue":"營收",
    #     # "grossProfits":	"毛利",
    #     # "profitMargins":"淨利率",
    #     # "operatingMargins":"營業利益率"
    # }


    fieldMap = {
        "公司名稱":info.get("longName"),
        "產業":info.get("sector"),
        "類型":typeDisp(info.get("typeDisp")),
        "開盤價":info.get("open"),
        "即時價格":info.get("currentPrice"),
        "昨收":info.get("regularMarketPreviousClose"),

        "當日最低":info.get("dayLow"),
        "當日最高":info.get("dayHigh"),
        "收盤價":info.get("Close"), 
        "市值":info.get("marketCap"),
        "本益比":info.get("trailingPE"),
        "預估本益比":info.get("forwardPE"),
        "殖利率":info.get("dividendYield"),
        "年配息":info.get("dividendRate"),
        "52週高": info.get("fiftyTwoWeekHigh"),
        "52週低": info.get("fiftyTwoWeekLow"),
    }
    # for key,value in info.items():
    #     if key in fieldMap:
    #       content += f"{fieldMap[key]}: {value}\n".
    for key,value in fieldMap.items():
        content+= f"{key}: {value}\n"
    return f"{announce} \n" + "\n"+ content

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