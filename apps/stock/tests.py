from django.test import TestCase
from .models import HotStock,FavoriteStock

class HotStockModelTest(TestCase):
    def setUp(self):
        HotStock.objects.create(stock_id = '0050',stock_name = '元大台灣50',suffix = 'TWO')

    def test_stock_can_insert(self):
        stock = HotStock.objects.create(stock_id = '0050',stock_name = '元大台灣50',suffix = 'TWO')
        stock.save()
        self.assertTrue(stock)

    # def test_stock_has_exist(self):


class FavoriteModelTest(TestCase):
    def setUp(self):
        FavoriteStock.objects.create(user_account=)