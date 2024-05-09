from logging import basicConfig
from urllib import request
from django.shortcuts import render
import requests

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime, timedelta

from cityList import city

weather_api = settings.WEATHER_ACCESS_TOKEN

def weatherAPI(location:str)->list:
      '''
      氣象局API(一般天氣預報，今明36小時天氣預報)
      URL:https://opendata.cwa.gov.tw/dist/opendata-swagger.html#/%E9%A0%90%E5%A0%B1/get_v1_rest_datastore_F_C0032_001

      1.城市名稱須完整顯示縣或市，例如高雄市、宜蘭縣。
      2.城市名稱必須是繁體字。
      3.若無城市名稱，預設為全部縣市

      * API時間區間改為取得當天資料。
      '''
      if location != "":
        # 替換簡體字
        # 若location非none且location中有"台"字
        if "台" in location:
          location = location.replace("台", "臺")

        cities = city()
        # 若location在cityList中有出現
        for s in range(len(cities)):
          try:
            if location == cities[s]:
            # Exact match
              location = cities[s]

          except Exception:
            # print(location+"不在可搜尋範圍內!!!!")
            return []

        # 時間區間
        current = datetime.now()
        nextDay = current + timedelta(1)
        new_period=nextDay.replace(hour=23, minute=0,second=0).strftime('%Y-%m-%dT%H:%M:%SZ')

        url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="
        response = requests.get(url + weather_api + "&locationName=" + location + "&timeFrom=" + current.strftime("%Y-%m-%dT%H:%M:%SZ")+"&timeTo="+new_period,timeout=5)

        response.raise_for_status()
        if response.status_code == 200 and response.headers["content-type"].strip().startswith("application/json"):
          data = response.json()

          dataDictList = []

          for place in data["records"]["location"]:  
            weatherDictList = []
            timeDictList = []
            minTemperatureDictList = []
            maxTemperatureDictList = []
            ciDictList = []
            popDictList = []

            for w in place['weatherElement']:
              for timeDict in w["time"]:
                timeDictList.append({
                  "startTime": timeDict["startTime"],
                  "endTime": timeDict["endTime"],
                })

              if w['elementName'] == "MinT":
                # 最低溫
                for timeDict in w["time"]:
                  minTemperatureDictList.append({
                    "value": timeDict['parameter']['parameterName'] #+timeDict['parameter']['parameterUnit']
                  })

              if w['elementName'] == "MaxT":
                # 最高溫
                for timeDict in w["time"]:
                  maxTemperatureDictList.append({
                    "value": timeDict['parameter']['parameterName']
                  })

              if w['elementName'] == "CI":
                for timeDict in w["time"]:
                  ciDictList.append({
                    "value": timeDict['parameter']['parameterName']
                  })
     
              if w['elementName'] == "Wx":
                # 天氣描述
                for timeDict in w["time"]:
                  weatherDictList.append({
                    "value": timeDict['parameter']['parameterName']
                  })

              if w['elementName'] == "PoP":
                # 降雨機率
                for timeDict in w["time"]:
                  popDictList.append({
                    "value": timeDict['parameter']['parameterName']+"%"
                  })
 
            tempDict = {
              "locationName": place["locationName"],
              "timeDictList": timeDictList[0],
              "weatherDictList": weatherDictList[0],
              "ciDictList":ciDictList[0],
              "minTemperatureDictList": minTemperatureDictList[0],
              "maxTemperatureDictList":maxTemperatureDictList[0],
              "popDictList":popDictList[0]
            } 
            dataDictList.append(tempDict)
          return dataDictList
      pass
