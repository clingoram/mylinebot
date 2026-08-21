from apps.bot.services.line_reply import reply
from linebot.models import TextSendMessage

def explain(event):
    '''
    說明
    '''

    disclaimer_text = """📌 使用說明與免責聲明
    本LINE Bot為個人side project，提供股票、天氣及新聞等資訊查詢功能。

    📈 股票資訊
    股票相關資料由第三方API取得，僅提供資訊查詢與資料整理，不構成任何投資、理財、買賣或其他金融建議。

    使用者應自行判斷並確認資料之正確性、完整性及即時性，本Bot不對任何因使用股票資訊所產生的投資決策或損失負責。

    ❓使用方式：
    股票股票代碼
    👉範例：
    股票2330

    📰 新聞資訊
    新聞資料來自公開新聞來源，僅提供標題、分類、時間及原文連結等資訊。
    完整內容請以原新聞來源為準。

    ❓使用方式：
    新聞 類別 欲搜尋之關鍵字。
    其中類別與關鍵字可選擇不輸入。
    👉範例：
    新聞 財經 台積電 
    或 
    新聞 財經

    🌦️ 天氣資訊
    天氣資料來自第三方API，實際天氣狀況可能與API資料有所差異。

    ❓使用方式：
    臺灣各縣市名稱
    👉範例：
    高雄市

    ⭐ 本Bot僅供個人side project使用，無任何投資理財目的。 ⭐"""

    reply(event.reply_token,TextSendMessage(text=disclaimer_text))