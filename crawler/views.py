from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json


# Create your views here.

def crawlerSomething():
  print('AAA')
  result = []
  # scroll_time = int(input('請輸入想要捲動幾次'))
  driver = webdriver.Chrome()

  driver.get("https://www.cakeresume.com/jobs?location_list%5B0%5D=Taiwan")
  # # title = driver.title
  # for now_time in range(1, scroll_time+1):
  driver.implicitly_wait(10)
  print(driver.title)
  #   print(f"now scroll {now_time}/{scroll_time}")
  element = driver.find_element(By.TAG_NAME, 'div')
  ele = element.find_element(By.CLASS_NAME, "JobSearchHits_list__3UtHp")
  # print(ele)
  result.append(ele)
  # for e in ele:
  #   try:
  #     title = e.find_element(By.CLASS_NAME,'JobSearchItem_headerTitle__CuE3V')
  #     href = e.get_attribute('href')
  #     result = {
  #       'title': title,
  #       'href': href,
  #        # 'subtitle': subtitle
  #     }
  #     result.append()
  #   except:
  #     pass

  driver.quit()
  return result