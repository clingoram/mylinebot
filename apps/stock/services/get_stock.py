import json

import yfinance as yf
from apps.stock.services.translate import translate

def getStock(stock_number:str):
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
    return translate(info,df)
