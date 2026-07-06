# import model
from apps.basic_info.models import Person,Message
from datetime import datetime

def insertKeyWord(user_id:str,keyword:str):
  '''
  儲存使用者在聊天室搜尋(關鍵字)
  '''
  if Person.objects.filter(account=user_id).exists():
    # 更新person的更新時間欄位
    person = Person.get(account=user_id)
    person.updatedAt = datetime.now()

    # 將user message(key word)存到message
    msg = Message(contentKeyWord = keyword,userAccount = person)
    msg.save()