'''
分流
'''
# from apps.weather.weather_service import get_weather
# # from apps.news.news_service import get_news
# # from apps.stock.service import get_stock


# def handle_message(text):

#     text = text.strip()

#     # 天氣
#     if text.startswith("天氣"):
#         city = text.replace("天氣", "").strip()
#         return get_weather(city)

#     # 新聞
#     if text == "新聞":
#         return get_news()

#     # 股票（純數字）
#     if text.isdigit():
#         return get_stock(text)

#     return "指令：天氣 台北 / 新聞 / 2330"