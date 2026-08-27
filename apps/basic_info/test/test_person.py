from django.test import TestCase
from apps.basic_info.models import Person
from apps.basic_info.services.actions import create_user

class PersonModelTests(TestCase):
  '''
  測試person
  '''
  def test_person_model_exists(self): 
    '''
    user account是否存在
    '''
    Person.objects.create(
      user_account = "test_user_001", 
      created_at = "2026-03-12"
    )
    person_count = Person.objects.count() 
    self.assertEqual(person_count, 1) 

  def test_create_user(self):
    '''
    建立使用者
    '''
    user_account = "test_user_001"
    result = create_user(userId=user_account)
    self.assertEqual(result, True)
    self.assertTrue(
      Person.objects.filter(
        user_account = user_account
      ).exists()
    )

  def test_create_user_duplicate_account(self):
    '''
    user account重複
    '''
    user_account = "test_user_002"
    Person.objects.create(
      user_account = user_account
    )
    result = create_user(userId=user_account)
    self.assertEqual(result, False)
    self.assertEqual(
      Person.objects.filter(
        user_account = user_account
      ).count(),1
    )