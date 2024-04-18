from django.db import models

# Create your models here.
from django.db.models.functions import Now

# Create your models here.
class User(models.Model):
  '''
  記錄使用者資訊
  '''
  # user id
  uid = models.CharField(max_length = 50, null = False)  
  # 使用者LINE名稱
  account = models.CharField(max_length = int(30), blank = False, null = False,editable = True)
  # 近期更新時間
  updated_at = models.DateTimeField(auto_now = True)
  # 建立時間
  created_at = models.DateTimeField(db_default = Now())

  def __str__(self):
    return self.account
  



class Message(models.Model):
  '''
  記錄使用者欲搜尋的訊息
  '''
  # user id
  user_d = models.ForeignKey(User, on_delete = models.CASCADE)
  # 訊息內容
  contentKeyWord = models.CharField(max_length=200)

  def __str__(self) -> str:
    return self.contentKeyWord