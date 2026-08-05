# Image
FROM python:3.12.3

# 設定工作目錄
WORKDIR /app

# 複製專案中的requirements.txt到容器中，以便安裝依賴
COPY requirements.txt /app/requirements.txt

# pip安裝所有Python
RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver

# 複製專案中的所有檔案到容器的工作目錄
COPY . .

# 執行Django開發伺服器，監聽所有IP (0.0.0.0) 的8000 port
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]