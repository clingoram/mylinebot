def translate(info:dict,df):
    '''
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