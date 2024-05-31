## 關於mylinebot

使用Django建置LINE機器人。
在本機開發時，使用ngrok建立https伺服器。

- 功能1:<br>
可依據使用者欲搜尋的臺灣城市，從氣象局API撈出對應的天氣資訊，目前取得的天氣時間資料區間為當天的資料。<br>
   <br>
  可搜尋氣象資訊的城市名單:<br>
   宜蘭縣,花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣

- 功能2:<br>
使用者在聊天室打上關鍵字「新聞」或「news」，可爬蟲財經新聞網站，取得5筆新聞。

將使用者line id以及在聊天室打上的字存至PostgreSQL資料庫內，目的主要是認為未來也許可以分析使用者習慣等。
此功能目前只有新增及更新。<br>
股票app已可取得台灣股票上市公司相關資訊，此功能尚未完成。
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
