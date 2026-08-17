from django.test import TestCase
from unittest.mock import patch
from apps.weather.services.flexMsg import flex_message

class FlexMsgTest(TestCase):
    @patch("apps.weather.services.flexMsg.weatherAPI")
    def test_flex_message_has_weather_data(self,mock_weather_api):
        '''
        mock weatherAPI()
        有資料是否正確產生Flex Message
        '''
        mock_weather_api.return_value = [
        {
            "locationName": "高雄市",
            "timeDictList": {
                "time": "08/17 12:00 - 08/17 18:00"
            },
            "weatherDictList": {
                "weather": "晴時多雲"
            },
            "ciDictList": {
                "ci": "舒適"
            },
            "minTemperatureDictList": {
                "min": "28"
            },
            "maxTemperatureDictList": {
                "max": "33"
            },
            "popDictList": {
                "pop": "20%"
            }
        }
        ]

        result = flex_message("高雄市")

        mock_weather_api.assert_called_once_with("高雄市")
        self.assertEqual(result["type"],"bubble")
        self.assertEqual(result["body"]["contents"][1]["text"],"高雄市")

    @patch("apps.weather.services.flexMsg.weatherAPI")
    def test_flex_message_no_weather_data(self, mock_weather_api):
        '''
        mock weatherAPI()
        沒有資料是否正確產生Flex Message
        '''
        mock_weather_api.return_value = []

        result = flex_message("小琉球")

        mock_weather_api.assert_called_once_with("小琉球")
        self.assertEqual(result,{})