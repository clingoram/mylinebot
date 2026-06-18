from urllib import request
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

def getPrice():
  '''
  取得所有股票當天股價
  '''
  url = 'https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL'
  response = requests.get(url)

  if response.status_code == 200 and response.headers["content-type"].strip().startswith("application/json"):
    data = response.json()
    return data