from hmac import new
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden

# Create your views here.
@csrf_exempt
def crawlerSomething(request):

  if request.method == "GET":
    news = []

    driver = webdriver.Chrome()
    driver.get("https://www.ctee.com.tw/livenews")
    element = driver.find_elements(By.CLASS_NAME,'newslist__card')
    for i in element:
      Dict = {}
      title = i.find_elements(By.CLASS_NAME,'news-title')
      type = i.find_elements(By.CLASS_NAME,'news-category')
      link = i.find_elements(By.CSS_SELECTOR,".news-title [href]")
      for j in link:
        lnk = j.get_attribute('href')

      Dict = {
        'title': title[0].text,
        'type': type[0].text,
        'link': lnk
      }
      news.append(Dict)
    print(news)

    # ----
    # driver.get("https://news.ltn.com.tw/list/breakingnews")
    # element = driver.find_elements(By.TAG_NAME,'li')
    # for i in element:
    #   Dict = {}
    #   title = i.find_elements(By.CLASS_NAME,'title')
    #   # link = i.find_elements(By.CSS_SELECTOR,".tit [href]")
    #   # for j in link:
    #   #   lnk = j.get_attribute('href')
    #   Dict = {
    #     'title': title,
    #     # 'type': type.text,
    #     # 'link': lnk
    #   }
    #   news.append(Dict)
    # print(news)

    driver.quit()
    # return result
    return HttpResponse()
  else:
    return HttpResponseBadRequest()
  


