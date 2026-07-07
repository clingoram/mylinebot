from apps.basic_info.models import Person,Message
from datetime import datetime

def create_user(userId:str):
  '''
  insert data into table
  '''
  Person.objects.create(user_account=userId)


def create_Keyword(user_id:str,keyword:str):
  '''
  儲存使用者在聊天室搜尋(關鍵字)
  '''
  if Person.objects.filter(user_account=user_id).exists():
    # 更新person的更新時間欄位
    person = Person.objects.filter(user_account=user_id).first()
    person.updated_at = datetime.now()

    # 將user message(key word)存到message
    Message.objects.create(keyword = keyword,user_account = person)