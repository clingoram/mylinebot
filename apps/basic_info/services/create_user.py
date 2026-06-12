from apps.basic_info.models import Person
from datetime import datetime

def create_user(request,id:str,name:str):
  '''
  insert data into table
  '''
  if request.method == 'POST':
    person = Person.objects.create(uid=id, account=name, created_at=datetime.now())
    person.save()
