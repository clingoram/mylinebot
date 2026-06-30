from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def crawlerSomething()->str:
    '''
    新聞爬蟲
    '''
    option = Options()
    option.add_argument("--headless=new")
    option.add_argument('blink-settings=imagesEnabled=false')
    option.add_argument("--disable-extensions")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=option)

    driver.get("https://www.ctee.com.tw/livenews")

    # 最多等5秒，若1秒就找到元素便立刻向下執行
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "newslist__card")
        )
    )

    content = ""
    element = driver.find_elements(By.CLASS_NAME,'newslist__card')
    for i in element[:5]:
        print("執行中...")
        try:
          # 新聞標題
          newsTitle = i.find_element(By.CLASS_NAME,"news-title").text
          # 新聞類型
          newsType = i.find_elements(By.CLASS_NAME,'news-category')
          # 新聞發佈時間
          time = i.find_elements(By.CLASS_NAME,"news-time")
          for j in time:
            newsTime = j.text

          # 新聞連結
          newsLink = i.find_element(By.CLASS_NAME,"news-title").get_attribute("href")

          content += "[{}] {}\n{}\n{}\n".format(newsType[0].text,newsTime,newsTitle, newsLink)

        except Exception as e:
          print("錯誤:",e)

    driver.quit()
    return content