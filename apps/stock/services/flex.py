from apps.stock.services.get_stock import getStock
def flex(key):
    '''
    flex message
    '''
    # call stock api
    stockO = getStock(key)

    contents = []

    for key, value in stockO.items():
        contents.append({
            "type": "box",
            "layout": "baseline",
            "contents": [
                {
                    "type": "text",
                    "text": key,
                    "size": "sm",
                    "color": "#888888",
                    "flex": 2
                },
                {
                    "type": "text",
                    "text": str(value),
                    "size": "sm",
                    "align": "end",
                    "flex": 3
                }
            ]
        })

    bubble = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": stockO["代碼"].strip(".TW"),
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "separator",
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": contents
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "action": {
                        "type": "postback",
                        "label": "加入追蹤",
                        "data": f"action=watch&stock_id={stockO['代碼']}"
                    }
                }
            ]
        }
    }
    return bubble