from hmac import new
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden

# Create your views here.
# @csrf_exempt
def crawlerSomething()->str:
  '''
  新聞爬蟲
  '''
  # if request.method == "GET":
  # news = []
  # option = Options()
  # # 無界面
  # option.add_argument("--headless") 
  # # 將選項加入Chrome中
  # driver = webdriver.Chrome(options=option)

  driver = webdriver.Chrome()
  driver.get("https://www.ctee.com.tw/livenews")
  driver.implicitly_wait(1)
  element = driver.find_elements(By.CLASS_NAME,'newslist__card')

  countData = 0
  content = ""
  for i in element:
    newsTitle = ""
    newsType = ""
    newsLink = ""
    newsTime = ""

    # Dict = {}
    if countData < 5:
      try:
        # 新聞標題
        newsTitle = i.find_elements(By.CLASS_NAME,'news-title')
        # 新聞類型
        newsType = i.find_elements(By.CLASS_NAME,'news-category')
        # 新聞發佈時間
        time = i.find_elements(By.CLASS_NAME,"news-time")
        for j in time:
          newsTime = j.text
        # 新聞連結
        link = i.find_elements(By.CSS_SELECTOR,".news-title [href]")
        for j in link:
          newsLink = j.get_attribute('href')

        content += "[{}] {}\n{}\n{}\n".format(newsType[0].text,newsTime,newsTitle[0].text, newsLink)
        countData += 1
      except:
          pass
    else:
      break

        # Dict = {
        #   'title': newsTitle[0].text,
        #   'time': newsTime,
        #   'type': newsType[0].text,
        #   'link': newsLink
        # }
        # news.append(Dict)
    # print(content)

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
  return content