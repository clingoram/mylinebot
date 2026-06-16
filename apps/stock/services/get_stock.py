import json

import yfinance as yf

def getStock(stock_number):
    '''
    取得https://github.com/ranaroussi/yfinance 台股資料
    但這資料value是英文

    stock 代碼可能不存在 => 打錯數字之類的
    '''
    stock = yf.Ticker(stock_number+".TW")  #台積電
    df = stock.history(period="1mo")
    # print(df)
    info = stock.info
    print(json.dumps(info, indent=4, ensure_ascii=False))
    
    content = ""
    fieldMap = {
        "city":"公司總部",
        "longName": "公司名稱",
        "sector": "產業",
        "industry": "子產業",
        "symbol":"股票代碼",
        "Open": "開盤價",
        "High": "最高價",
        "Low": "最低價",
        "Close": "收盤價",
        "Adj Close": "調整收盤價",
        "Volume": "成交量",

        "marketCap": "市值",
        "trailingPE": "本益比",
        "forwardPE": "預估本益比",
        "dividendYield": "殖利率",
    }
    for key,value in info.items():
        if key in fieldMap:
          content += f"{fieldMap[key]}: {value}\n"
    return content
   