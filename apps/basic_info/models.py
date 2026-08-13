from django.db import models
from django.db.models.functions import Now
from django.core.validators import RegexValidator


# Database table
class Person(models.Model):
  '''
  table Person
  記錄使用者資訊
  '''
  # LINE User ID
  user_account = models.CharField(unique=True,max_length = int(150), blank = False, null = False,validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]*$',
            message='Account must be Alphanumeric',
            code='invalid_Account'
        ),
    ])
  # 建立時間
  created_at = models.DateTimeField(auto_now_add=True)
  # 近期更新時間
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.user_account
  
  class Meta:
    db_table = 'person'
  
  @classmethod
  def create_user(self, user_account):
    person = self.create(user_account=user_account)
    return person


class Message(models.Model):
  '''
  table Message
  記錄使用者欲搜尋的訊息
  '''
  user_account = models.ForeignKey(Person,db_column='user_account',on_delete=models.CASCADE)
  # 訊息內容
  keyword = models.CharField(max_length=200)
  # 建立時間
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self) -> str:
    return self.keyword
  
  class Meta:
    db_table = 'message'
    
  @classmethod
  def create_message(self,user_account):
    msg = self.create(user_account = user_account)
    return msg
  