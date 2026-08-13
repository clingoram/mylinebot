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

### 技術

- Django
- LINE Bot
- PostgreSQL
- Selenium
- Docker

## 機器人回覆:

![image](https://github.com/clingoram/mylinebot/blob/master/images/S__34291716.jpg "氣象訊息回覆 - 不在可查詢範圍內")
![image](https://github.com/clingoram/mylinebot/blob/master/images/weather.jpg "氣象查詢地區回覆")
![image](https://github.com/clingoram/mylinebot/blob/master/images/crawler_reply.jpg "新聞爬蟲")
![image](https://github.com/clingoram/mylinebot/blob/master/images/search_stock.jpeg "查詢股票")
![image](https://github.com/clingoram/mylinebot/blob/master/images/list_follow_stock.jpeg "列出追蹤的所有股票清單")

### Container Diagram

![image](https://github.com/clingoram/mylinebot/blob/master/images/Container_Diagram.png "架構圖")

### ER Diagram

![image](https://github.com/clingoram/mylinebot/blob/master/images/ER_Diagram.png "ER Diagram")

### Development Automation

Webhook Auto-Configuration Flow
![image](https://github.com/clingoram/mylinebot/blob/master/images/Webhook_Auto_Configuration_Flow.png "Webhook Auto-Configuration Flow")

### Modular Design

將Weather、Stock、Crawler拆成獨立Service。
降低模組耦合，方便測試與擴充。

### Database Design

使用PostgreSQL設計多對多資料模型。
支援使用者追蹤多支股票。

# Docker 開發環境

本專案使用 Docker Compose 啟動 Django、PostgreSQL 與 ngrok，不需要另外建立 Python virtual environment 或手動啟動 ngrok。

## 啟動專案

### 第一次啟動或修改 Docker 設定

第一次建立 Docker container，或修改以下檔案後，需要重新 build：

- `docker-compose.yml`
- `Dockerfile`
- `requirements.txt`

執行：

```bash
docker compose up --build
```

### 一般啟動

如果沒有修改 Docker 設定，直接執行：

```bash
docker compose up
```

啟動後會自動建立並啟動：

- Django container
- PostgreSQL container
- ngrok container

Django 啟動時會自動更新 LINE Webhook，因此不需要再手動執行：

- Python virtual environment
- ngrok

## 關閉專案

```bash
docker compose down
```

這會停止並移除目前由 Docker Compose 建立的 containers。

---

## Database Migration

### 修改 `models.py`

當 `models.py` 有修改時，需要先建立 migration：

```bash
docker compose exec django python3 manage.py makemigrations
```

接著執行 migration：

```bash
docker compose exec django python3 manage.py migrate
```

也可以依序執行：

```bash
docker compose exec django python3 manage.py makemigrations
docker compose exec django python3 manage.py migrate
```

---

## 執行 Test

執行 Django Test：

```bash
docker compose exec django python3 manage.py test
```

其中 `django` 是 `docker-compose.yml` 中 Django service 的名稱：

```yaml
services:
  django: ...
```

如果未來修改 service 名稱，例如：

```yaml
services:
  web: ...
```

則 Test 指令需要改成：

```bash
docker compose exec web python3 manage.py test
```

---

## 常用指令整理

| 用途                           | 指令                                                          |
| ------------------------------ | ------------------------------------------------------------- |
| 第一次啟動 / Docker 設定有修改 | `docker compose up --build`                                   |
| 一般啟動                       | `docker compose up`                                           |
| 關閉                           | `docker compose down`                                         |
| 建立 migration                 | `docker compose exec django python3 manage.py makemigrations` |
| 執行 migration                 | `docker compose exec django python3 manage.py migrate`        |
| 執行 Test                      | `docker compose exec django python3 manage.py test`           |

<hr>

- [氣象局](https://opendata.cwa.gov.tw/dist/opendata-swagger.html) <br>
- [Django Doc.](https://docs.djangoproject.com/en/5.0/) <br>
- [Line-bot-sdk-python](https://line-bot-sdk-python.readthedocs.io/en/stable/index.html) <br>
- [ngrok](https://ngrok.com/)
- [selenium](https://github.com/seleniumhq/selenium)
- PostgreSQL
