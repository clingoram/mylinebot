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
    stock_id = models.CharField(max_length=100,unique=True,blank=False)
    stock_name = models.CharField(max_length=200,blank=False)
    suffix = models.CharField(max_length=50,db_comment='.TW 或 .TWO',default="TW")

    class Meta:
        db_table = 'hot_stock'

class FavoriteStock(models.Model):
    '''
    user收藏的stock
    id,userAccount,stockId

    userAccount is relationship with id of table Person
    stockId relationship with id of table HotStock
    '''
    user_account = models.ForeignKey('basic_info.person',db_column='user_account',db_comment='對應Person id',on_delete=models.CASCADE)
    # stockId = models.ForeignKey(HotStock, on_delete=models.CASCADE)
    stock_id = models.CharField(max_length=100,unique=True,blank=False)


    class Meta:
        db_table = 'favorite_stock'