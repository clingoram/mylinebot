# import model
from apps.basic_info.models import Person,Message
from datetime import datetime

def insertKeyWord(user_id:str,keyword:str):
  '''
  儲存使用者在聊天室搜尋(關鍵字)
  '''
  if Person.objects.filter(id=user_id).exists():
    # 更新person的更新時間欄位
    person = Person.objects.get(id=user_id)
    person.updated_at = datetime.now()
    person.save()

    # 將user message(key word)存到message
    msg = Message.objects.create(id = person, contentKeyWord = keyword,created_at = datetime.now())
    msg.save()