import requests

def getCompanyInfo():
  '''
  取得台灣所有上市公司基本資料
  '''
  jsonFile = 'https://openapi.twse.com.tw/v1/opendata/t187ap03_L'
  response = requests.get(jsonFile)

  if response.status_code == 200 and response.headers["content-type"].strip().startswith("application/json"):
    return response.json() 