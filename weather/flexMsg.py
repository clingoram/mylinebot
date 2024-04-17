from weather.weather import weatherAPI

def flex_message(location:str)->dict:
  '''
  Line bot flex message
  將氣象API回傳的資料塞入flex message內
  '''
  # 取氣象API資料
  weatherData = weatherAPI(location)

  for i in weatherData:
    # 城市名稱
    name = i['locationName']
    # 天氣概況
    des = ""
    # 最低溫
    minTemperature = ""
    # 最高溫
    maxTemperature = ""
    # 降雨機率
    rain = ""
    # 區間
    rangeData = ""
    # 舒適度
    ci = ""
    for ele in i['timeDictList'].values():
      rangeData += ele + " "

    for ele in i['weatherDictList'].values():
      des = ele

    for ele in i['ciDictList'].values():
      ci = ele
    for ele in i['minTemperatureDictList'].values():
      minTemperature = ele

    for ele in i['maxTemperatureDictList'].values():
      maxTemperature = ele

    for ele in i['popDictList'].values():
      rain = ele

  content = {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "地點",
            "weight": "bold",
            "color": "#1DB446",
            "size": "sm"
          },
          {
            "type": "text",
            "text": name,
            "weight": "bold",
            "size": "xxl",
            "margin": "md"
          },
          {
            "type": "text",
            "text": rangeData,
            "size": "md",
            "color": "#aaaaaa",
            "wrap": True
          },
          {
            "type": "separator",
            "margin": "xxl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "xxl",
            "spacing": "sm",
            "contents": [
               {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "概況",
                    "size": "sm",
                    "color": "#555555",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": des,
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "舒適度",
                    "size": "sm",
                    "color": "#555555",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": ci,
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "溫度",
                    "size": "sm",
                    "color": "#555555",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": minTemperature + "~" + maxTemperature + "°C",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "降雨機率",
                    "size": "sm",
                    "color": "#555555",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": rain,
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                  }
                ]
              }
            ]
          }
        ]
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  return content