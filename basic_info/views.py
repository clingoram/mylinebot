from django.shortcuts import render
# import model
from basic_info.models import Person,Message
from datetime import datetime


# Create your views here.
def create_user(request,id:str,name:str):
  '''
  建立person(user)
  '''
  if request.method == 'POST':
    person = Person.objects.create(uid=id, account=name, created_at=datetime.now())
    person.save()

def insertKeyWord(user_id:str,keyword:str):
  '''
  儲存使用者在聊天室搜尋(關鍵字)
  '''
  if Person.objects.filter(uid=user_id).exists():
    # 將user message存到message
    person = Person.objects.get(uid=user_id)
    person.updated_at = datetime.now()
    person.save()

    # person.uid
    msg = Message.objects.create(uid = person, contentKeyWord = keyword,created_at = datetime.now())
    msg.save()