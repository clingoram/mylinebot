from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def crawler_news(keyword=None)->str:
    '''
    新聞爬蟲
    '''
    # TODO:無法抓取資料
    option = Options()
    option.add_argument("--headless=new")
    option.add_argument('blink-settings=imagesEnabled=false')
    option.add_argument("--disable-extensions")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=option)

    driver.get("https://www.ctee.com.tw/livenews")

    # 最多等20秒，若1秒就找到元素便立刻向下執行
    WebDriverWait(driver, 20).until(
      EC.presence_of_element_located((By.CLASS_NAME, "newslist__card"))
    )
    # id wrap -> id main -> class content__body -> class newslist livenews -> newslist__card
    content = ""
    element = driver.find_elements(By.CLASS_NAME,"newslist__card")
    for i in element[:5]:
        print("執行中...")
        try:
          # 新聞標題
          newsTitle = i.find_element(By.CLASS_NAME,"news-title").text
          if keyword:
            if keyword not in newsTitle:
                continue
          # 新聞類型
          newsType = i.find_element(By.CLASS_NAME, "news-category").text
          # 新聞發佈時間
          newsTime = i.find_element(By.CLASS_NAME, "news-time").text

          # 新聞連結
          newsLink = i.find_element(By.CLASS_NAME,"news-title").get_attribute("href")

          content += "[{}] {}\n{}\n{}\n".format(newsType[0].text,newsTime,newsTitle, newsLink)

        #   content += (
        #     f"[{i['type']}]\n"
        #     f"{i['time']}\n"
        #     f"{i['title']}\n"
        #     f"{i['url']}\n\n"
        # )

        except Exception as e:
          print(f"錯誤: {e}")

        finally:
          driver.quit()
    return content