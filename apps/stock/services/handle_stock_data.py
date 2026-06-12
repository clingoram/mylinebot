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