# Image
FROM python:3.12.3

# 設定工作目錄
WORKDIR /app

# 複製專案中的 requirements.txt 到容器中，以便安裝依賴
COPY requirements.txt /app/requirements.txt

# 使用 pip 安裝所有 Python 依賴
RUN pip3 install -r requirements.txt

# 複製專案中的所有檔案到容器的工作目錄
COPY . .

# 執行 Django 開發伺服器，監聽所有 IP (0.0.0.0) 的 8000 port
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]