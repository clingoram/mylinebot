from django.test import TestCase
from unittest.mock import Mock, patch
from apps.weather.services.weather_api import weatherAPI

class WeatherAPITest(TestCase):
    
    @patch("apps.weather.services.weather_api.requests.get")
    def test_api_request(self,mock_get):
        '''
        mock HTTP request
        '''
        mock = Mock()
        location = "高雄市"
        token= "test-token"
        weatherAPI(location)