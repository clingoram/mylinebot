from django.test import TestCase
from datetime import datetime
from .models import Person,Message

# Create your tests here.
class PersonModelTests(TestCase):
  '''
  測試person
  '''
  def setUp(self):
    Person.objects.create(user_account = 'U21d04568JjfkdjfLjioklkd915f1d',created_at='2026-3-12')
  
  def test_perosn_model_exists(self):
    person = Person.objects.count()
    self.assertEqual(person,0)

  def test_person_insert(self):
    '''
    test insert into table.
    '''
    person = Person.objects.create(user_account="U21d",account="testuser",createdAt=datetime.now())
    person.save()
    self.assertTrue(person)

  def test_person_update(self):
    '''
    test to update table person updated_at column
    '''
    user_id = "U21d04568JjfkdjfLjioklkd915f1d"
    if Person.objects.filter(user_account = user_id).exists():
      person = Person.objects.get(user_account=user_id)
      person.updatedAt = datetime.now()
      person.save()
      self.assertTrue(person)
    else:
      self.assertFalse(False)

  

class MessageModelTests(TestCase):
  '''
  測試message
  '''
  def test_message_model_exists(self):
    msg = Message.objects.count()
    self.assertEqual(msg,0)