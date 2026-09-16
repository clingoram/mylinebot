from django.db import models

# Create your models here.
class HotStock(models.Model):
    '''
    熱門台股
    id,stock_id,stock_name,suffix

    eg. 
    id:1
    stock_id:2330
    stock_name:xxx
    suffix:TW
    '''
    stock_id = models.CharField(max_length=100,unique=True,blank=False)
    stock_name = models.CharField(max_length=200,blank=False)
    suffix = models.CharField(max_length=50,db_comment='.TW 或 .TWO',default="TW")

    class Meta:
        db_table = 'hot_stock'

class FavoriteStock(models.Model):
    '''
    user收藏的stock
    id,user_account,stock_id

    user_account is relationship with id of table Person
    stock_id
    '''
    user_account = models.ForeignKey('basic_info.person',db_column='user_account',db_comment='對應Person id',on_delete=models.CASCADE)
    # stockId = models.ForeignKey(HotStock, on_delete=models.CASCADE)
    stock_id = models.CharField(max_length=100,blank=False)


    class Meta:
        db_table = 'favorite_stock'
        # 同一個使用者（user_account）不能重複收藏同一檔股票（stock_id）
        constraints = [
            models.UniqueConstraint(
                fields=["user_account", "stock_id"],
                name="unique_person_stock"
            )
        ]