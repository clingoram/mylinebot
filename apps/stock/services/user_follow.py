from apps.basic_info.models import Person
from apps.stock.models import FavoriteStock


def userFollowList(userId:str,stockId):
    '''
    user 追蹤股票
    依據user id取得該user追蹤的所有股票名稱
    '''

    FavoriteStock.objects.get_or_create(userId=userId,stock_no=stockId)
    
