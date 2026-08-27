from apps.stock.models import HotStock
from typing import Any
import re
import requests
import logging
logger = logging.getLogger(__name__)

# =========================
# Private
# =========================
def _clean_stock_id(stock_id: str) -> str:
    '''
    清理使用者輸入的股票代碼
    只保留英文字母與數字
    '''
    stock_id = stock_id.strip()

    # 如果使用者輸入2330.TW / 2330.TWO
    stock_id = re.sub(r"\.(TW|TWO)$", "",stock_id, flags=re.IGNORECASE)

    # 移除其他非英數字元
    stock_id = re.sub(r"[^a-zA-Z0-9]", "",stock_id)

    return stock_id.upper()


def _suffix_from_db(stock_id:str) -> HotStock | None:
    '''
    先從table找對應資料
    '''
    find = HotStock.objects.filter(stock_id = stock_id).first()
    if find is None:
        return None
    return find

def _save_into_db(stock_id:str,stock_name:str,suffix:str) -> bool:
    '''
    代碼、名稱、suffix存進table
    '''
    HotStock.objects.create(stock_id = stock_id,stock_name = stock_name,suffix = suffix)
    return True

def _fetch_api_data(stock_id:str) -> dict[str, Any] | None:
    '''
    負責call API拿原始英文資料
    取得https://github.com/ranaroussi/yfinance 資料
    https://finance.yahoo.com/

    但這資料是英文，部份須轉換成中文

    yfinance 台股代號後面須加上.TW或.TWO，例如：1234.TW
    '''
    import yfinance as yf

    find = _suffix_from_db(stock_id=stock_id)
    # print(find)
    # logger.info(find)

    # =========================
    # DB 有資料
    # =========================
    if find is not None:
        symbol = f"{find.stock_id}.{find.suffix}"
        stock = yf.Ticker(symbol)
        df = stock.history(period="5d",auto_adjust=False)
        if df.empty:
            return None

        info = stock.info
        if not info:
            return None

        # print(f"找table內資料: {find.stock_name} -- {find.stock_id}.{find.suffix}")
        logger.info(f"找table內資料: {find.stock_name} -- {find.stock_id}.{find.suffix}")

        
        # Yahoo 沒有資料
        if df.empty:
            # print(f"Yahoo找不到資料：{symbol}")
            logger.info(f"找不到資料： {symbol}")
            return None

        # info 沒資料
        if not info:
            # print(f"Yahoo info沒有資料：{symbol}")
            logger.info(f"沒有資料：{symbol}")
            return None
    
        return _map_eng_to_chinese(info, df)

    # =========================
    # DB 沒資料
    # =========================
    for suffix in ("TW", "TWO"):
        symbol = f"{stock_id}.{suffix}"
        # print(f"找API: {symbol}")
        logger.info(f"找API: {symbol}")

        try:
            stock = yf.Ticker(symbol)
            df = stock.history(period="5d",auto_adjust=False)

            # 沒資料 → 嘗試下一個suffix
            if df.empty:
                continue

            info = stock.info

            # 沒有info → 嘗試下一個suffix
            if not info:
                continue
            # print(info)

            getSuffix = info["symbol"].split(".")[-1]
            _save_into_db(stock_id=stock_id,stock_name=info.get("shortName", ""),suffix=getSuffix)
            return _map_eng_to_chinese(info=info, df =df)

        except Exception as e:
            # print(f"{symbol} 查詢失敗：{e}")
            logger.warning(f"{symbol} 查詢失敗：{e}")
            continue

    # TW/TWO都找不到
    return None


def _get_stock_change(data:dict) -> dict[str, float]:
    '''
    資料處理
    讀取API的漲跌欄位

    ⚠️若資料格式差不多，可以萬用
    '''
    change = data.get('regularMarketChange')
    change_percent = data.get('regularMarketChangePercent')
    
    # 如果欄位不存在，人工計算
    if change is None or change_percent is None:
        # 取得當前價格（防呆機制）
        current_price = data.get('currentPrice') or data.get('regularMarketPrice')
        previous_close = data.get('previousClose')
        
        if current_price and previous_close:
            change = current_price - previous_close
            # 計算百分比並四捨五入到小數點後兩位
            change_percent = (change / previous_close) * 100
            
    return {
        'change': round(change, 2) if change else 0.0,
        'change_percent': round(change_percent, 2) if change_percent else 0.0
    }

def _map_eng_to_chinese(info:dict,df) -> dict[str, Any]:
    '''
    資料處理
    ⭐股票domain專用的共用function
    負責mapping 原始資料（英文）資訊成中文資料（內部私有）
    '''
    
    # announce = "⚠️ 此line bot之股票資料是從API取得。只提供股票相關資訊且用於個人side-project，不具有任何投資理財目的。 ⚠️"

    try:
        change = _get_stock_change(data = info)

        latest_close = None

        if df is not None and not df.empty and "Close" in df.columns:
            latest_close = float(df["Close"].iloc[-1])
        else:
            latest_close = (
                info.get("currentPrice")
                or info.get("regularMarketPrice")
            )

        fieldMap = {
            "代碼": info.get("symbol", "").split(".")[0],
            "公司名稱": info.get("shortName"),
            "產業": _sectorDisp(sector=info.get("sector")),
            "細分產業": _fmt_num(value=info.get("industry")),
            "類型": _typeDisp(info_type=info.get("typeDisp")),

            "即時價格": info.get("currentPrice"),
            "昨收": info.get("regularMarketPreviousClose"),

            "當日最低": info.get("dayLow"),
            "當日最高": info.get("dayHigh"),
            "收盤價": latest_close,

            "漲跌": change.get("change"),
            "漲跌幅": change.get("change_percent"),

            "本益比": _fmt_num(value=info.get("trailingPE")),
            "預估本益比": _fmt_num(value=info.get("forwardPE")),

            "殖利率": _fmt_num(value=info.get("dividendYield")),
            "年配息": _fmt_num(value=info.get("dividendRate")),
            "52週高": info.get("fiftyTwoWeekHigh"),
            "52週低": info.get("fiftyTwoWeekLow"),
            # "說明":"※ 以上資訊僅供參考，不構成投資或理財建議。"
        }

        # print(fieldMap)

        return fieldMap

    except Exception as e:
        logger.exception(f"Map error: {type(e).__name__}")
        logger.exception(e)
        raise

def _typeDisp(info_type: str | None) -> str:
    '''
    資料處理
    股票類型 
    '''
    stockType = {
        "Equity":"普通股票",
        "ETF":"指數型基金",
        "Index":"指數",
        "Cryptocurrency":"加密貨幣",
        "Future":"期貨",
        "Currency":"外匯"
    }
    # for key,value in stockType.items():
    #     if infoType == key:
    #         return value
    # return None
    if not info_type:
            return "N/A"

    return stockType.get(info_type, info_type)

def _sectorDisp(sector: str | None) -> str:
    '''
    資料處理
    產業類型
    '''
    sectorType = {
        "Technology": "科技",
        "Financial Services": "金融服務",
        "Healthcare": "醫療保健",
        "Industrials": "工業",
        "Consumer Cyclical": "非必需消費品",
        "Consumer Defensive": "必需消費品",
        "Energy": "能源",
        "Basic Materials": "基礎材料",
        "Communication Services": "通訊服務",
        "Utilities": "公用事業",
        "Real Estate": "房地產",
    }
    if not sector:
        return "N/A"

    return sectorType.get(sector, sector)
     
def _fmt_num(value) -> str:
    '''
    資料處理
    Flex Message顯示用
    None或空字串顯示N/A
    '''
    if value is None or value == "":
        return "N/A"

    return str(value)

# =========================
# Public API
# =========================
def get_stock_flex_message(key):
    '''
    flex message (單一股票)

    主要對外接口，給router.py用於「單檔股票查詢」 -> 顯示用

    串聯： _clean_stock_id() -> Call API(_fetch_api_data()) -> 轉中文(_map_eng_to_chinese()) -> 塞入這個Flex Message
    '''
    # try: 
    clean_stock_id = _clean_stock_id(stock_id=key)
    stockO = _fetch_api_data(stock_id=clean_stock_id)
    # print(stockO)
    if not stockO:
        return "無資料"

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
                    "text": stockO["代碼"],
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
                    },
                }
            ]
        }
    }
    return bubble
    # except requests.RequestException:
    #     logger.exception(f"尋找 {key} 失敗")
    #     return None