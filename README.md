# mylinebot

一個使用**Django**開發的LINE Bot，提供天氣查詢、股票追蹤與新聞整合功能。

使用者可以透過LINE查詢天氣資訊、取得新聞及追蹤個股。系統整合多個外部API與資料來源，並使用**LINE Flex Message**呈現資訊。

本專案使用**Docker Compose**整合Django、PostgreSQL與ngrok，並透過啟動腳本自動取得ngrok URL、更新LINE Webhook。因此開發時不需要另外建立Python虛擬環境、手動啟動ngrok或在每次重新啟動後手動設定Webhook

---

## Features

### 1. 天氣查詢

使用者可以輸入臺灣城市名稱，系統會透過**中央氣象署 Open Data API**取得對應的天氣資訊。

目前提供**當日天氣資訊**查詢。

支援的城市：

- 宜蘭縣
- 花蓮縣
- 臺東縣
- 澎湖縣
- 金門縣
- 連江縣
- 臺北市
- 新北市
- 桃園市
- 臺中市
- 臺南市
- 高雄市
- 基隆市
- 新竹縣
- 新竹市
- 苗栗縣
- 彰化縣
- 南投縣
- 雲林縣
- 嘉義縣
- 嘉義市
- 屏東縣

### 2. 新聞

使用者在LINE聊天室輸入：

```text
新聞
```

或：

```text
新聞 類別 關鍵字
```

系統會從新聞網站中取得最新相關新聞，並透過LINE Text Message呈現。
類別：
政治，財經，社會，娛樂，體育，科技，生活，國際、健康

其中類別與欲搜尋之關鍵字可選擇不輸入。

### 3. 股票追蹤

使用者在LINE聊天室輸入：

```text
股票 股票代碼
```

或：

```text
股票股票代碼
```

可以透過LINE Flex Message：

- 追蹤股票
- 取消追蹤股票
- 查詢目前追蹤的股票清單
- 查看追蹤股票的相關資訊

系統使用PostgreSQL儲存使用者與股票的追蹤關係。

### 4. 說明

使用者輸入「說明」可看到本line bot相關說明。

## Testing

All tests passed successfully.

```text
✓ 37 tests passed
```

## Tech Stack

### Backend

- **Python**
- **Django**
- **LINE Messaging API / LINE Bot SDK**

### Database

- **PostgreSQL**

### Data & Integration

- **yfinance** — 取得股票價格、漲跌幅等市場資訊
- **Beautiful Soup** — 取得新聞
- **中央氣象署 Open Data API** — 取得天氣資訊

### Infrastructure

- **Docker**
- **Docker Compose**
- **ngrok**

### Testing & CI

- **Django Test**
- **unittest.mock**
- **GitHub Actions**

---

## System Architecture

### DEMO

<video src="https://github.com/user-attachments/assets/8b9c2397-4e61-4741-bc82-9ada72a16920" width="100%" controls autoplay loop muted></video>

### 機器人回覆

![image](https://github.com/clingoram/mylinebot/blob/master/images/S__34291716.jpg "氣象訊息回覆 - 不在可查詢範圍內")
![image](https://github.com/clingoram/mylinebot/blob/master/images/weather.jpg "氣象查詢地區回覆")

<!-- ![image](https://github.com/clingoram/mylinebot/blob/master/images/crawler_reply.jpg "新聞爬蟲") -->

![image](https://github.com/clingoram/mylinebot/blob/master/images/news.jpeg "新聞")

<!-- ![image](https://github.com/clingoram/mylinebot/blob/master/images/search_stock.jpeg "查詢股票並加入追蹤名單") -->

![image](https://github.com/clingoram/mylinebot/blob/master/images/stock_reply_search.jpeg "查詢股票")
![image](https://github.com/clingoram/mylinebot/blob/master/images/list_follow_stock.jpeg "列出追蹤的所有股票清單")

### Container Diagram

<!-- ![image](https://github.com/clingoram/mylinebot/blob/master/images/Container_Diagram.png "架構圖") -->

![image](https://github.com/clingoram/mylinebot/blob/master/images/container_diagram_8_21.png "架構圖")

### ER Diagram

![image](https://github.com/clingoram/mylinebot/blob/master/images/er_diagram_8_31_update.png "ER Diagram")

### Development Automation

Webhook Auto-Configuration Flow
![image](https://github.com/clingoram/mylinebot/blob/master/images/webhook_Auto-Configuration_Flow_8_21.png "Webhook Auto-Configuration Flow")

---

## Design

### Modular Design

將主要功能拆分為獨立Service：

- Weather
- Stock
- News

透過模組化設計降低元件之間的耦合，使各功能可以獨立開發、測試與擴充。

### Database Design

使用**PostgreSQL**設計資料模型，支援使用者與股票之間的多對多關係。

一個使用者可以追蹤多支股票，而同一支股票也可以被多個使用者追蹤。

---

# Development

本專案使用Docker Compose管理開發環境。以下說明專案的啟動、關閉、Database Migration及測試方式。

## 啟動專案

### 第一次啟動或修改Docker設定

第一次建立Docker containers或修改以下檔案時，需要重新build：

- `docker-compose.yml`
- `Dockerfile`
- `requirements.txt`

執行：

```bash
docker compose up --build
```

### 一般啟動

如果沒有修改Docker設定，可以直接執行：

```bash
docker compose up
```

---

## 關閉專案

```bash
docker compose down
```

此指令會停止並移除目前由Docker Compose建立的containers。

---

## Database Migration

當Django Model有修改時，需要重新建立並套用migration。

### 建立migration

```bash
docker compose exec django python3 manage.py makemigrations
```

### 執行migration

```bash
docker compose exec django python3 manage.py migrate
```

也可以依序執行：

```bash
docker compose exec django python3 manage.py makemigrations
docker compose exec django python3 manage.py migrate
```

---

## Testing

執行Django Test：

```bash
docker compose exec django python3 manage.py test
```

其中`django`是`docker-compose.yml`中Django service的名稱：

```yaml
services:
  django: ...
```

如果未來將Django service名稱修改為`web`：

```yaml
services:
  web: ...
```

則Test指令需要改成：

```bash
docker compose exec web python3 manage.py test
```

---

## Common Commands

| 用途                          | 指令                                                          |
| ----------------------------- | ------------------------------------------------------------- |
| 第一次啟動 / Docker設定有修改 | `docker compose up --build`                                   |
| 一般啟動                      | `docker compose up`                                           |
| 關閉                          | `docker compose down`                                         |
| 建立migration                 | `docker compose exec django python3 manage.py makemigrations` |
| 執行migration                 | `docker compose exec django python3 manage.py migrate`        |
| 執行Test                      | `docker compose exec django python3 manage.py test`           |

---

## References

- [中央氣象署 Open Data](https://opendata.cwa.gov.tw/dist/opendata-swagger.html)
- [Django Documentation](https://docs.djangoproject.com/en/6.0/)
- [LINE Bot SDK for Python](https://line-bot-sdk-python.readthedocs.io/en/stable/index.html)
- [ngrok](https://ngrok.com/)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#)
- [PostgreSQL](https://www.postgresql.org/)
