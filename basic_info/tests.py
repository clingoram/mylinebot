from django.test import TestCase
from datetime import datetime
from .models import Person,Message

# Create your tests here.
class PersonModelTests(TestCase):
  def test_perosn_model_exists(self):
    person = Person.objects.count()
    self.assertEqual(person,0)


  def test_person_insert(self):
    '''
    test insert into table.
    '''
    person = Person.objects.create(uid="U21d0250e1363b12368796b2430bd0190",account="testuser",created_at=datetime.now())
    person.save()
    self.assertTrue(person)

  

class MessageModelTests(TestCase):
  def test_message_model_exists(self):
    msg = Message.objects.count()
    self.assertEqual(msg,0)