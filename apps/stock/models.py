from django.db import models

# Create your models here.
class HotStock(models.Model):
    '''
    熱門台股
    id,stock_code,stock_name

    eg. 
    id:1
    stock_code:2330
    stock_name:xxx
    '''
    stockCode = models.CharField(max_length=100,unique=True,blank=False)
    stockName = models.CharField(max_length=200,blank=False)

class FavoriteStock(models.Model):
    '''
    user收藏的stock
    id,user_id,stock_id

    user_id relationship with Person
    stock_id relationship with HotStock id
    '''
    userId = models.ForeignKey('basic_info.Person', to_field="account",db_column="userAccount",on_delete=models.CASCADE)
    stockId = models.ForeignKey(HotStock, on_delete=models.CASCADE)