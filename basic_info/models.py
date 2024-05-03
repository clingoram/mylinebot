from django.db import models
from django.db.models.functions import Now
from django.core.validators import RegexValidator

# Create your models here.
class Person(models.Model):
  '''
  記錄使用者資訊
  '''
  # user id
  uid = models.CharField(max_length = 50, null = False,unique = True)  
  # 使用者LINE名稱
  account = models.CharField(max_length = int(30), blank = False, null = False,editable = True,validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]*$',
            message='Account must be Alphanumeric',
            code='invalid_Account'
        ),
    ])
  # 近期更新時間
  updated_at = models.DateTimeField(auto_now = True)
  # 建立時間
  created_at = models.DateTimeField(db_default = Now())

  # def __str__(self):
  #   return self.account
  
  # class Meta:
  #   db_table = "info_person"
  
  # @classmethod
  # def create_message(self,uid):
  #   msg = self.create(uid = uid)
  #   return msg


class Message(models.Model):
  '''
  記錄使用者欲搜尋的訊息
  '''
  # user id
  uid = models.ForeignKey('Person', on_delete = models.CASCADE,to_field='uid',null = True, blank = True)
  # 訊息內容
  contentKeyWord = models.CharField(max_length=200)
  # 建立時間
  created_at = models.DateTimeField(db_default = Now())
  
  # def __str__(self) -> str:
  #   return self.contentKeyWord
  
  # class Meta:
  #   db_table = "info_message"
    
  # @classmethod
  # def create_message(self,uid):
  #   msg = self.create(uid = uid)
  #   return msg
  