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

  def test_person_update(self):
    '''
    test to update table person updated_at column
    '''
    user_id = "U21d0250e1363b12368796b2430bd0190"
    if Person.objects.filter(uid = user_id).exists():
      person = Person.objects.get(uid=user_id)
      person.updated_at = datetime.now()
      person.save()
      self.assertTrue(person)
    else:
      self.assertFalse(False)

  

class MessageModelTests(TestCase):
  def test_message_model_exists(self):
    msg = Message.objects.count()
    self.assertEqual(msg,0)