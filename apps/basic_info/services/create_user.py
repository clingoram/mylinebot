from apps.basic_info.models import Person
from datetime import datetime

def create_user(request,userId:str):
  '''
  insert data into table
  '''
  if request.method == 'POST':
    person = Person.objects.create(account=userId)
    person.save()
