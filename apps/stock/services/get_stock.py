import json

import yfinance as yf
from apps.stock.services.translate import translate

def getStock(stock_number):
    '''
    取得https://github.com/ranaroussi/yfinance 台股資料
    但這資料value是英文

    '''
    stock = yf.Ticker(stock_number+".TW") # yfinance 台股代號須加上.TW

    # stock 代碼可能不存在 => 打錯數字之類的
    df = stock.history(period="5d")
    if df.empty:
        return "查無該股票存在"
    
    info = stock.info
    print(info.get("longName"))
    if not info:
       return "查無該股票存在"

    print(json.dumps(info, indent=4, ensure_ascii=False))

    return translate(info)
