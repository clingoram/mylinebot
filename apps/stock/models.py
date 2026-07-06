from django.db import models

# Create your models here.
class HotStock(models.Model):
    '''
    熱門台股
    id,stockId,stockName

    eg. 
    id:1
    stockId:2330
    stockName:xxx
    '''
    stockId = models.CharField(max_length=100,unique=True,blank=False)
    stockName = models.CharField(max_length=200,blank=False)

class FavoriteStock(models.Model):
    '''
    user收藏的stock
    id,userAccount,stockId

    userAccount is relationship with id of table Person
    stockId relationship with id of table HotStock
    '''
    userAccount = models.ForeignKey('basic_info.Person', to_field="account",db_column="userAccount",on_delete=models.CASCADE)
    # stockId = models.ForeignKey(HotStock, on_delete=models.CASCADE)
    stockId = models.CharField(max_length=100,unique=True,blank=False)