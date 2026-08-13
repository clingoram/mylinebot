from django.http import JsonResponse,HttpResponse
from apps.basic_info.models import Person
from apps.stock.models import FavoriteStock
from apps.stock.services.quotes import _fetch_api_data

# =========================
# Public
# =========================
def follow_stock(userId:str,stockId:str):
    '''
    增加追蹤股票
    依據user id取得該user追蹤的所有股票名稱
    '''
    person = Person.objects.filter(user_account=userId).first()

    if person is None:
        return HttpResponse("User not found", status=404)

    FavoriteStock.objects.create(user_account=person,stock_id=stockId)

    return HttpResponse("OK!!", status=200)


def unfollow_stock(userId:str,stockId:str):
    '''
    取消追蹤
    '''
    # 找到那一筆追蹤紀錄並刪除
    deleted_count, _ = FavoriteStock.objects.filter(user_account = userId,stock_id = stockId).delete()
    
    if deleted_count > 0:
        return HttpResponse("已取消追蹤",status=200)
        # return JsonResponse({"message": "已取消追蹤"},status = 200)
    # return JsonResponse({"error": "該股票不在追蹤名單中"},status = 404)
    return HttpResponse("該股票不在追蹤名單中",status=404)


def get_user_stocks_list(userId:str):
    '''
    取得使用者追蹤的所有股票清單
    '''
    # 先從Person找尋對應id
    person_id = Person.objects.filter(user_account = userId).values_list('id', flat=True).first()
    # 取得該使用者追蹤的所有股票清單
    user_stocks = FavoriteStock.objects.filter(user_account=person_id).values_list('stock_id', flat=True)
    
    stock_data_list = []
    for code in user_stocks:
        # 呼叫股票API並取得mapping後的中文資料
        data = _fetch_api_data(code) 
        if data:
            stock_data_list.append(data)
            
    # 丟給底下產生flex message
    return get_flex_message_contents(stock_data_list)


def get_flex_message_contents(stock_data_list):
    '''
    flex message 追蹤清單
    '''
    bubbles = []
    page_size = 5  # 每張卡片最多5檔股票
    # print(stock_data_list)
    
    for i in range(0, len(stock_data_list), page_size):
        chunk = stock_data_list[i:i+page_size]
        page_num = (i // page_size) + 1
        
        # 單張卡片的基本結構
        bubble = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#111111",
                "contents": [
                    {"type": "text", "text": f"📊 我的追蹤清單 ({page_num})", "weight": "bold", "size": "lg"}
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": []
            }
        }
        
        # 一張卡片塞入5檔股票
        for stock in chunk:
            # print("目前處理的股票資料:", stock, "型態是:", type(stock)) 
            
            # ：如果這筆資料是dict，就跳過不處理
            if not isinstance(stock, dict):
                continue
                
            # 取得漲跌欄位，並強制轉換成float，避免字串跟0比較時崩潰
            try:
                change_val = float(stock.get("漲跌", 0.0)) if stock.get("漲跌") is not None else 0.0
            except (ValueError, TypeError):
                change_val = 0.0

            if change_val > 0:
                color = "#FF3B30"
                change_text = f"+{stock['漲跌']}%"
            elif change_val < 0:
                color = "#28A745"
                change_text = f"{stock['漲跌']}%"
            else:
                color = "#8E8E93"
                change_text = "0.00%"
                
            row = {
                "type": "box",
                "layout": "horizontal",
                "alignment": "center",
                "contents": [
                    # 左半邊：名稱與代碼
                    {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 3, 
                        "contents": [
                            {"type": "text", "text": str(stock["公司名稱"]), "weight": "bold", "size": "md"},
                            {"type": "text", "text": str(stock["代碼"]), "size": "xs", "color": "#8E8E93"}
                        ]
                    },
                    # 右半邊：現價、漲跌幅以及取消追蹤按鈕
                    {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 2,
                        "align": "end",
                        "contents": [
                            {"type": "text", "text": str(stock["即時價格"]), "weight": "bold", "size": "md"},
                            {"type": "text", "text": change_text, "size": "xs", "color": color, "weight": "bold"},
                             # 取消追蹤按鈕
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label": "取消追蹤",
                                    "data": f"action=unfollow&stock_id={stock['代碼']}",
                                    # "displayText": f"取消追蹤 {stock['公司名稱']}"  # 使用者點擊時對話框顯示的文字
                                },
                                "style": "secondary",
                                "color": "#F2F2F7",
                                "height": "sm",
                                "margin": "xs"
                            }
                        ]
                    }
                ]
            }
            bubble["body"]["contents"].append(row)
            bubble["body"]["contents"].append({"type": "separator", "margin": "md"})
            
        if bubble["body"]["contents"] and bubble["body"]["contents"][-1]["type"] == "separator":
            bubble["body"]["contents"].pop()
            
        # 將做好的卡片append進陣列
        bubbles.append(bubble)
    
    # 如果只有1張，直接回傳bubble；如果多張，外層要包一層carousel
    if len(bubbles) == 1:
        flex_contents = bubbles[0]
    else:
        flex_contents = {
            "type": "carousel",
            "contents": bubbles[:10]  # 最多能放10張bubble
        }
    return flex_contents