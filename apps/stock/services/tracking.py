from django.http import JsonResponse
from apps.basic_info.models import Person
from apps.stock.models import FavoriteStock
from apps.stock.services.quotes import get_stock_realtime_data


def follow_stock(userId:str,stockId):
    '''
    增加追蹤股票
    依據user id取得該user追蹤的所有股票名稱
    '''

    if Person.objects.filter(user_account=userId).exists():
        person = Person.objects.filter(user_account=userId).first()

        FavoriteStock.objects.create(user_account=person,stock_id=stockId)

# ❌
def list_favorite_stocks(userId):
    '''
    列出使用者股票清單
    '''
    # 撈出該使用者所有的追蹤股票(部份股價資料)
    stocks = FavoriteStock.objects.filter(user_account_id=userId).values_list('stock_id', flat=True)
    
    return JsonResponse({"stocks": list(stocks)})
# ❌
# def unfollow_stock(userId,stockId):
#     '''
#     取消追蹤
#     '''
#     stock_code = request.POST.get(stockId) # 假設從前端傳來要刪除的股票代碼
    
#     # 找到那一筆特定的追蹤紀錄並刪除
#     deleted_count, _ = FavoriteStock.objects.filter(
#         user_account_id=userId, 
#         stock_code=stock_code
#     ).delete()
    
#     if deleted_count > 0:
#         return JsonResponse({"message": "Successfully removed"})
#     return JsonResponse({"error": "Stock not found in favorites"}, status=404)

# ❌
def get_user_stocks_message(user_id):
    # 1. 從自家的資料庫拿到自選股清單（例如 ['2330', '2454']）
    user_stocks = FavoriteStock.objects.filter(user_account_id=user_id).values_list('stock_code', flat=True)
    
    stock_data_list = []
    for code in user_stocks:
        # 2. 跨檔案呼叫公有窗口，拿到整齊的中文資料 Dict
        data = get_stock_realtime_data(code) 
        if data:
            stock_data_list.append(data)
            
    # 3. 丟給同檔案底下的 Flex 產生器
    return build_favorite_stock_list_flex(stock_data_list)

# ❌
def build_favorite_stock_list_flex(stock_data_list):
    """
    追蹤清單
    
    stock_data_list 傳入的格式範例:
    [
        {"code": "2330", "name": "台積電", "price": "1005", "change_percent": "+1.5", "trend": "up"},
        {"code": "2454", "name": "聯發科", "price": "1210", "change_percent": "-0.8", "trend": "down"},
    ]
    """
    
    # flex Message
    bubble = {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {"type": "text", "text": "📊 我的追蹤清單", "weight": "bold", "size": "lg", "color": "#111111"}
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md", # 每一列之間空出適當間距
            "contents": []
        }
    }
    
    # 動態將使用者追蹤的股票一檔一檔塞進去
    for stock in stock_data_list:
        # 根據漲跌決定顏色（台灣習慣紅漲綠跌，海外相反，可自行調整）
        color = "#FF3B30" if stock["trend"] == "up" else "#34C759" if stock["trend"] == "down" else "#8E8E93"
        
        row = {
            "type": "box",
            "layout": "horizontal",
            "alignment": "center",
            "contents": [
                # 左半邊：名稱與代碼
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {"type": "text", "text": stock["name"], "weight": "bold", "size": "md"},
                        {"type": "text", "text": stock["code"], "size": "xs", "color": "#8E8E93"}
                    ]
                },
                # 右半邊：現價與漲跌幅
                {
                    "type": "box",
                    "layout": "vertical",
                    "align": "end",
                    "contents": [
                        {"type": "text", "text": stock["price"], "weight": "bold", "size": "md"},
                        {"type": "text", "text": f"{stock['change_percent']}%", "size": "xs", "color": color}
                    ]
                }
            ]
        }
        bubble["body"]["contents"].append(row)
        
        # 幫每檔股票中間加一條淡淡的淡淡的分隔線，視覺上更整齊
        bubble["body"]["contents"].append({"type": "separator", "margin": "md"})
        
    # 移除最後一條多餘的分隔線
    if bubble["body"]["contents"]:
        bubble["body"]["contents"].pop()
        
    return bubble