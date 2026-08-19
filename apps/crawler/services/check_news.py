def checkNews():
    '''
    檢查時間：讀取資料庫中第一筆資料的scraped_at。判斷是否過期：
        沒過期（< 10分鐘）：直接從PostgreSQL撈出這10筆新聞丟回給Line使用者。
        已過期（> 10分鐘）：Python爬蟲發動，抓取最新的10筆新聞。
    
    清空並覆寫：在Django中使用LatestNews.objects.all().delete()全部清空，然後將新抓到的10筆資料bulk_create()寫入。
    '''