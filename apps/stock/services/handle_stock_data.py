from urllib import request
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

from apps.stock.services.get_company_info import getCompanyInfo
from apps.stock.services.get_price import getPrice

import yfinance as yf

# @csrf_exempt
def combineStockData():
    '''
    結合getCompanyInfo和getPrice
    '''
    #   if request.method == "GET":
    information = getCompanyInfo()
    price = getPrice()

    for (a,b) in zip(information,price):
        stockContent = {}
        if isinstance(a['公司代號'], str) and isinstance(b['Code'], str):
            code = a['公司代號']
            fullName = a['公司名稱']
            name = a['公司簡稱']
            industry = a['產業別']

            open = b['OpeningPrice']
            highest = b['HighestPrice']
            lowest = b['LowestPrice']
            close = b['ClosingPrice']

            stockContent = {
                'code': code,
                'fullName': fullName,
                'name': name,
                'industry': industry,
                'open': open,
                'highest': highest,
                'lowest': lowest,
                'close': close
            }
        print(stockContent)

    return HttpResponse("OK!!",status=200)
#   else:
#     return HttpResponse("Something wrong...",status=405)

def getStock(stock_number):
    stock = yf.Ticker("2300.TW")  #台積電
    df = stock.history(period="1mo")
    print(df)
    info = stock.info
    # print(info['city'])
    for key, value in info.items():
        return map['city']
        # print(key)
    return "H"
        

def map():
    fieldMap = {
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

        "longName": "公司名稱",
        "sector": "產業",
        "industry": "子產業",
    }
    return fieldMap