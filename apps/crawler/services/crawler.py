# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import requests
from bs4 import BeautifulSoup

def crawler_news(keyword=None, category=None, limit=10):
    '''
    SETN 新聞爬蟲

    keyword  : 搜尋新聞標題關鍵字
    category : 新聞類型，例如「財經」、「社會」
    limit    : 最多取得幾筆
    '''
    url = "https://www.setn.com/viewall"
    
# Selenium
# def crawler_news(keyword=None)->str:
#     '''
#     新聞爬蟲
#     '''
#     # TODO:無法抓取資料
#     option = Options()
#     option.add_argument("--headless=new")
#     option.add_argument('blink-settings=imagesEnabled=false')
#     option.add_argument("--disable-extensions")
#     option.add_argument("--no-sandbox")
#     option.add_argument("--disable-gpu")
#     driver = webdriver.Chrome(options=option)

#     content = ""
#     try:
        
#       driver.get("https://www.setn.com/viewall")
#       # print(driver.page_source)

#       # 最多等20秒，若1秒就找到元素便立刻向下執行
#       # WebDriverWait(driver, 20).until(
#       #   EC.presence_of_element_located((By.CLASS_NAME, "newslist__card"))
#       # )
#       WebDriverWait(driver, 20).until(
#         EC.visibility_of_any_elements_located(
#           (By.CSS_SELECTOR, ".newslist__card")
#         )
#       )
      
      
#       # element = driver.find_elements(By.CLASS_NAME,"newslist__card")
#       elements = driver.find_elements( By.CSS_SELECTOR,".news_list_item")
#     # news_info
#       print(f"找到 {len(elements)} 筆新聞")
#       for i,element in elements[:5]:
#           print("執行中...")
#           try:
#             # 新聞標題
#             newsTitle = i.find_element(By.CLASS_NAME,"title title_mobile").text
#             if keyword:
#               if keyword not in newsTitle:
#                   continue
#             # 新聞類型
#             newsType = i.find_element(By.CLASS_NAME, "tab smart-link").text
#             # 新聞發佈時間
#             newsTime = i.find_element(By.CLASS_NAME, "time").text
            
#             # 新聞連結
#             try:
#               newsLink = element.find_element(By.CSS_SELECTOR,".smart-link a").get_attribute("href")
#             except Exception:
#               newsLink = element.find_element(By.CSS_SELECTOR,"a").get_attribute("href")

#             content += (
#                 f"[{newsType}]\n"
#                 f"{newsTime}\n"
#                 f"{newsTitle}\n"
#                 f"{newsLink}\n\n"
#             )

#           except Exception as e:
#             print(f"⚠️ 第 {i + 1} 筆錯誤: {e}")

#     except Exception as e:
#       print(f"⚠️ 爬蟲錯誤: {e}")

#     finally:
#       driver.quit()

#     return content




