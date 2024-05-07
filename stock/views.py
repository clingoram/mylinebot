from urllib import request
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import requests
import csv
import os
import itertools 
def getCompanyInfo():
  '''
  取得台灣所有上市公司基本資料
  '''
  url = 'https://openapi.twse.com.tw/v1/opendata/t187ap03_L'
  response = requests.get(url)

  if response.status_code == 200 and response.headers["content-type"].strip().startswith("application/json"):
     return response.json() 

def getPrice():
  '''
  取得所有股票當天股價
  '''
  url = 'https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL'
  response = requests.get(url)

  if response.status_code == 200 and response.headers["content-type"].strip().startswith("application/json"):
    data = response.json()
    return data

@csrf_exempt
def combineStockData(request):
  '''
  結合getCompanyInfo和getPrice
  '''
  if request.method == "GET":
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

    return HttpResponse()
  else:
    return HttpResponseBadRequest()