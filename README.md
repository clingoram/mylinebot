## 關於mylinebot

使用Django建置LINE機器人，可依據使用者欲搜尋的臺灣城市，從氣象局API撈出對應的天氣資訊，目前取得的天氣時間資料區間為當天的資料。
使用ngrok建立https伺服器。

可搜尋的城市名單:<br>
宜蘭縣,花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣


## Requirement:
- Django >= 5.0
- line-bot-sdk-python
- ngrok(for localhost)

## 機器人回覆:
![image](https://github.com/clingoram/mylinebot/blob/master/images/S__33816579.jpg "氣象訊息回覆")
![image](https://github.com/clingoram/mylinebot/blob/master/images/crawler_reply.jpg "新聞爬蟲")

## Ref:
- [氣象局](https://opendata.cwa.gov.tw/dist/opendata-swagger.html) <br>
- [Django Doc.](https://docs.djangoproject.com/en/5.0/) <br>
- [Line-bot-sdk-python](https://line-bot-sdk-python.readthedocs.io/en/stable/index.html) <br>
- [ngrok](https://ngrok.com/)
