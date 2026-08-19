from django.test import TestCase, override_settings
from unittest.mock import Mock, patch
from apps.weather.services.weather_api import weatherAPI

@override_settings(WEATHER_ACCESS_TOKEN="test-token")
class WeatherAPITest(TestCase):
    '''
    test of weather api
    '''

    @patch("apps.weather.services.weather_api.requests.get")
    def test_weather_api_with_location(self, mock_get):
        '''
        指定城市
        '''
        location = "臺南市"
        # 模擬API response
        mock_response = Mock()

        mock_response.status_code = 200
        mock_response.headers = {
            "content-type": "application/json"
        }

        mock_response.json.return_value = {
            "records": {
                "location": [
                    {
                        "locationName": "臺南市",
                        "weatherElement": [
                            {
                                "elementName": "MinT",
                                "time": [
                                    {
                                        "startTime": "2026-08-17T12:00:00+08:00",
                                        "endTime": "2026-08-17T18:00:00+08:00",
                                        "parameter": {
                                            "parameterName": "28"
                                        }
                                    }
                                ]
                            },
                            {
                                "elementName": "MaxT",
                                "time": [
                                    {
                                        "startTime": "2026-08-17T12:00:00+08:00",
                                        "endTime": "2026-08-17T18:00:00+08:00",
                                        "parameter": {
                                            "parameterName": "33"
                                        }
                                    }
                                ]
                            },
                            {
                                "elementName": "CI",
                                "time": [
                                    {
                                        "startTime": "2026-08-17T12:00:00+08:00",
                                        "endTime": "2026-08-17T18:00:00+08:00",
                                        "parameter": {
                                            "parameterName": "舒適"
                                        }
                                    }
                                ]
                            },
                            {
                                "elementName": "Wx",
                                "time": [
                                    {
                                        "startTime": "2026-08-17T12:00:00+08:00",
                                        "endTime": "2026-08-17T18:00:00+08:00",
                                        "parameter": {
                                            "parameterName": "晴時多雲"
                                        }
                                    }
                                ]
                            },
                            {
                                "elementName": "PoP",
                                "time": [
                                    {
                                        "startTime": "2026-08-17T12:00:00+08:00",
                                        "endTime": "2026-08-17T18:00:00+08:00",
                                        "parameter": {
                                            "parameterName": "20"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }

        mock_get.return_value = mock_response

        result = weatherAPI(location)

        # print("result:", result)
        # print("type:", type(result))

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["locationName"], "臺南市")
        kwargs = mock_get.call_args.kwargs

        self.assertEqual(kwargs["params"]["locationName"],"臺南市")

    @patch("apps.weather.services.weather_api.requests.get")
    def test_weather_api_default_location(self, mock_get):
        '''
        測使用預設城市
        '''
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {
            "content-type": "application/json"
        }

        mock_response.json.return_value = {
            "records": {
                "location": []
            }
        }

        mock_get.return_value = mock_response

        weatherAPI("")

        mock_get.assert_called_once()

        kwargs = mock_get.call_args.kwargs

        # 確認用預設城市
        self.assertEqual(kwargs["params"]["locationName"],"高雄市")


    @patch("apps.weather.services.weather_api.requests.get")
    def test_not_zh_TW(self,mock_get):
        '''
        城市名稱非繁體中文
        '''
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {
            "content-type": "application/json"
        }
        mock_response.json.return_value = {
            "records": {
                "location": []
            }
        }

        mock_get.return_value = mock_response

        weatherAPI("台北市")

        kwargs = mock_get.call_args.kwargs

        self.assertEqual(kwargs["params"]["locationName"],"臺北市")

