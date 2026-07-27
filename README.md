## 關於mylinebot
一個使用Django開發的LINE Bot，可提供天氣查詢、股票追蹤及財經新聞整合。
使用者可透過LINE查詢資訊、追蹤個股，系統會整合多個外部API並以Flex Message呈現。

撰寫啟動腳本，自動取得ngrok URL並更新LINE Webhook，省去每次重新啟動後的手動設定流程。

### 功能

- 功能1:<br>
  可依據使用者欲搜尋的臺灣城市，從氣象局API撈出對應的天氣資訊，目前取得的天氣時間資料區間為當天的資料。<br>
  <br>
  可搜尋氣象資訊的城市名單:<br>
  宜蘭縣,花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣

- 功能2:<br>
  使用者在聊天室打上關鍵字「新聞」或「news」，可爬蟲財經新聞網站，取得5筆新聞。

- 功能3:<br>
  股票追蹤，使用者在Flex Message可追蹤與取消追蹤股票。亦可查詢目前追蹤股票清單相關資訊。

### Modular Design
將Weather、Stock、Crawler拆成獨立Service。
降低模組耦合，方便測試與擴充。

### Database Design
使用PostgreSQL設計多對多資料模型。
支援使用者追蹤多支股票。

### 技術

- Django
- LINE Bot
- PostgreSQL
- Selenium
- Docker

### How to run:
Terminal 1: ngrok http 8000
Terminal 2(啟動虛擬機後): python3 manage.py run_dev

<hr>

- [氣象局](https://opendata.cwa.gov.tw/dist/opendata-swagger.html) <br>
- [Django Doc.](https://docs.djangoproject.com/en/5.0/) <br>
- [Line-bot-sdk-python](https://line-bot-sdk-python.readthedocs.io/en/stable/index.html) <br>
- [ngrok](https://ngrok.com/)
- [selenium](https://github.com/seleniumhq/selenium)
- PostgreSQL

## 機器人回覆:

![image](https://github.com/clingoram/mylinebot/blob/master/images/S__34291716.jpg "氣象訊息回覆 - 不在可查詢範圍內")
![image](https://github.com/clingoram/mylinebot/blob/master/images/weather.jpg "氣象查詢地區回覆")
![image](https://github.com/clingoram/mylinebot/blob/master/images/crawler_reply.jpg "新聞爬蟲")
