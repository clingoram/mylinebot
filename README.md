# mylinebot

一個使用 **Django** 開發的 LINE Bot，提供天氣查詢、股票追蹤與財經新聞整合功能。

使用者可以透過 LINE 查詢天氣資訊、取得財經新聞、追蹤個股。系統整合多個外部 API 與資料來源，並使用 **LINE Flex Message** 呈現資訊。

本專案同時整合 **Docker、PostgreSQL 與 ngrok**，並撰寫啟動腳本自動取得 ngrok URL、更新 LINE Webhook，省去每次重新啟動後手動設定 Webhook 的流程。

---

## Features

### 1. 天氣查詢

使用者可以輸入臺灣城市名稱，系統會透過 **中央氣象署 Open Data API** 取得對應的天氣資訊。

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

### 2. 財經新聞

使用者在 LINE 聊天室輸入：

```text
新聞
```

或：

```text
news
```

系統會爬取財經新聞網站，取得最新的 5 筆財經新聞，並透過 LINE Flex Message 呈現。

### 3. 股票追蹤

使用者可以透過 LINE Flex Message：

- 追蹤股票
- 取消追蹤股票
- 查詢目前追蹤的股票清單
- 查看追蹤股票的相關資訊

系統使用 PostgreSQL 儲存使用者與股票的追蹤關係。

---

## Tech Stack

- Django
- LINE Bot SDK
- PostgreSQL
- Selenium
- Docker
- ngrok

---

## System Architecture

### Robot Response

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

---

## Design

### Modular Design

將主要功能拆分為獨立 Service：

- Weather
- Stock
- Crawler

透過模組化設計降低元件之間的耦合，使各功能可以獨立開發、測試與擴充。

### Database Design

使用 **PostgreSQL** 設計資料模型，支援使用者與股票之間的多對多關係。

一個使用者可以追蹤多支股票，而同一支股票也可以被多個使用者追蹤。

---

# Docker 開發環境

本專案使用 **Docker Compose** 啟動 Django、PostgreSQL 與 ngrok，不需要另外建立 Python virtual environment，也不需要手動啟動 ngrok。

## Prerequisites

開始使用前，請先安裝：

- Docker
- Docker Compose

並確認 Docker 已正常運作。

---

## 啟動專案

### 第一次啟動或修改 Docker 設定

第一次建立 Docker containers，或修改以下檔案時，需要重新 build：

- `docker-compose.yml`
- `Dockerfile`
- `requirements.txt`

執行：

```bash
docker compose up --build
```

### 一般啟動

如果沒有修改 Docker 設定，可以直接執行：

```bash
docker compose up
```

啟動後會自動建立並啟動：

- Django container
- PostgreSQL container
- ngrok container

Django 啟動時會自動取得 ngrok URL 並更新 LINE Webhook，因此不需要再手動：

- 建立或啟動 Python virtual environment
- 啟動 ngrok
- 手動設定 LINE Webhook

---

## 關閉專案

執行：

```bash
docker compose down
```

此指令會停止並移除目前由 Docker Compose 建立的 containers。

---

# Database Migration

## 修改 `models.py`

當 Django Model 有修改時，需要重新建立 migration。

### 1. 建立 migration

```bash
docker compose exec django python3 manage.py makemigrations
```

### 2. 執行 migration

```bash
docker compose exec django python3 manage.py migrate
```

也可以依序執行：

```bash
docker compose exec django python3 manage.py makemigrations
docker compose exec django python3 manage.py migrate
```

---

# Testing

執行 Django Test：

```bash
docker compose exec django python3 manage.py test
```

其中：

```text
django
```

是 `docker-compose.yml` 中 Django service 的名稱：

```yaml
services:
  django: ...
```

如果未來將 Django service 名稱修改為：

```yaml
services:
  web: ...
```

則 Test 指令需要改成：

```bash
docker compose exec web python3 manage.py test
```

---

# Common Commands

| 用途                           | 指令                                                          |
| ------------------------------ | ------------------------------------------------------------- |
| 第一次啟動 / Docker 設定有修改 | `docker compose up --build`                                   |
| 一般啟動                       | `docker compose up`                                           |
| 關閉                           | `docker compose down`                                         |
| 建立 migration                 | `docker compose exec django python3 manage.py makemigrations` |
| 執行 migration                 | `docker compose exec django python3 manage.py migrate`        |
| 執行 Test                      | `docker compose exec django python3 manage.py test`           |

---

# References

- [中央氣象署 Open Data](https://opendata.cwa.gov.tw/dist/opendata-swagger.html)
- [Django Documentation](https://docs.djangoproject.com/en/5.0/)
- [LINE Bot SDK for Python](https://line-bot-sdk-python.readthedocs.io/en/stable/index.html)
- [ngrok](https://ngrok.com/)
- [Selenium](https://github.com/seleniumhq/selenium)
- [PostgreSQL](https://www.postgresql.org/)
