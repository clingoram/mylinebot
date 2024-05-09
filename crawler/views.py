from hmac import new
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden


def crawlerSomething()->str:
    '''
    新聞爬蟲
    '''
    # option = Options()
    # option.add_argument("--headless=new")
    # option.add_argument('blink-settings=imagesEnabled=false')
    # option.add_argument("--disable-extensions")
    # option.add_argument("--no-sandbox")
    # option.add_argument("--disable-gpu")
    # driver = webdriver.Chrome(options=option)

    driver = webdriver.Chrome()
    driver.get("https://www.ctee.com.tw/livenews")
    driver.implicitly_wait(2)
    element = driver.find_elements(By.CLASS_NAME,'newslist__card')

    countData = 0
    content = ""
    for i in element:
        newsTitle = ""
        newsType = ""
        newsLink = ""
        newsTime = ""
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

    driver.quit()
    return content