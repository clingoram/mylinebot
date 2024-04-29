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
    result = {}

    # scroll_time = int(input('請輸入想要捲動幾次'))
    driver = webdriver.Chrome()

    # driver.get("https://www.cakeresume.com/jobs?location_list%5B0%5D=Taiwan")

    # driver.implicitly_wait(10)
    # # for now_time in range(1, scroll_time+1):
    # title = driver.title
    # print(title)
    # #   print(f"now scroll {now_time}/{scroll_time}")
    # element = driver.find_element(By.TAG_NAME, 'div')
    # ele = element.find_elements(By.CLASS_NAME, "JobSearchHits_list__3UtHp")
    # print(ele)
    # result.append(ele)


    driver.get("https://www.ctee.com.tw/livenews")
    element = driver.find_elements(By.CLASS_NAME,'newslist__card')#.send_keys("webElement")
    # ele = element.find_elements(By.TAG_NAME, "h3")
    # attr = driver.find_elements(By.CLASS_NAME,'news-title')

    for i in element:

      # title = i.find_elements(By.CSS_SELECTOR,'h3 .news-title')
      # title= i.find_elements(By.TAG_NAME, "h3")
      title = i.find_elements(By.CLASS_NAME,'news-title')
    #   # text = title.get_attribut('href')
      
      result = {
          'title': title,
          # 'href': text,
        }
    print(result)


    # for e in ele:
    #   print(e)
      # try:
      #   title = e.find_element(By.CLASS_NAME,'JobSearchItem_headerTitle__CuE3V')
      #   href = e.get_attribute('href')
      #   result = {
      #     'title': title,
      #     'href': href,
      #      # 'subtitle': subtitle
      #   }
      #   result.append()
      # except:
      #   pass

    driver.quit()
    # return result
    return HttpResponse()
  else:
    return HttpResponseBadRequest()