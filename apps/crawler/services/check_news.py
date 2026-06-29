def checkNews():
    '''
       
    檢查時間：讀取資料庫中第一筆資料的 scraped_at。判斷是否過期：
    沒過期（< 10分鐘）：直接從 PostgreSQL 撈出這 10 筆新聞丟回給 Line 使用者。（完全不 call 外部網路、不執行爬蟲，速度極快！）
    已過期（> 10分鐘）：Python 爬蟲立刻發動，抓取最新的 10 筆新聞。
    
    清空並覆寫：在 Django 中使用 LatestNews.objects.all().delete() 全部清空，然後將新抓到的 10 筆資料 bulk_create() 寫入。
    '''