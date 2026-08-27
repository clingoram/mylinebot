# Image
FROM python:3.12.3

# 設定工作目錄
WORKDIR /app

# 複製專案中的requirements.txt到容器中，以便安裝依賴
COPY  requirements.txt .

# pip安裝所有Python
RUN pip3 install --no-cache-dir -r requirements.txt

# 複製專案中的所有檔案到容器的工作目錄
COPY . .