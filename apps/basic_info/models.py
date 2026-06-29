from django.db import models
from django.db.models.functions import Now
from django.core.validators import RegexValidator


# Database table
class Person(models.Model):
  '''
  table Person
  記錄使用者資訊
  '''
  # 使用者LINE名稱
  account = models.CharField(unique=True,max_length = int(150), blank = False, null = False,validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]*$',
            message='Account must be Alphanumeric',
            code='invalid_Account'
        ),
    ])
  # 建立時間
  createdAt = models.DateTimeField(auto_now_add=True)
  # 近期更新時間
  updatedAt = models.DateTimeField(auto_now = True)

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
  table Message
  記錄使用者欲搜尋的訊息
  '''
  userAccount = models.ForeignKey(Person,to_field="account",db_column="userAccount",on_delete=models.CASCADE)
  # 訊息內容
  contentKeyWord = models.CharField(max_length=200)
  # 建立時間
  createdAt = models.DateTimeField(auto_now_add=True)
  
  # def __str__(self) -> str:
  #   return self.contentKeyWord
  
  # class Meta:
  #   db_table = "info_message"
    
  # @classmethod
  # def create_message(self,uid):
  #   msg = self.create(uid = uid)
  #   return msg
  