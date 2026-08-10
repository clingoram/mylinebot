from django.test import TestCase
from datetime import datetime
from .models import Person,Message
from apps.basic_info.services.actions import create_user,create_Keyword

# 可測試model以及views.py(services/)邏輯

class PersonModelTests(TestCase):
  '''
  測試person
  '''
  def test_person_model_exists(self): 
    '''
    user_account是否存在
    '''
    Person.objects.create(user_account = "test_user_001", created_at = "2026-03-12")
    person_count = Person.objects.count() 
    self.assertEqual(person_count, 1) 

  def test_create_user(self): 
    user_account = "test_user_001"
    result = create_user(user_account)
    self.assertEqual(result, 200)
    self.assertTrue(
        Person.objects.filter(
          user_account = user_account
        ).exists()
    )

  def test_create_user_duplicate_account(self):
    '''
    重複user_account
    '''
    user_account = "test_user_002"
    Person.objects.create(user_account = user_account)
    result = create_user(user_account)
    self.assertEqual(result, 400)
    self.assertEqual(
        Person.objects.filter(
          user_account = user_account
        ).count(),
        1
    )

class MessageModelTests(TestCase):
  '''
  測試key word message
  '''
  def test_message_model_exists(self):
    msg = Message.objects.count()
    self.assertEqual(msg,0)

  def test_create_Keyword_when_user_exists(self):
    '''
    user存在，message可以建立
    '''
    Person.objects.create(
      user_account = "test_user_001", 
      created_at = "2026-03-12"
    )
    keyword = "Test"
    person = Person.objects.get(user_account = "test_user_001")

    result = create_Keyword(person.user_account,keyword)
    self.assertEqual(result, 200)
    self.assertTrue(
      Message.objects.filter(user_account = person).exists()
    )


  def test_cannot_create_keyword_when_user_not_exists(self):
    '''
    user不存在，不能insert 到 message
    '''
    user_account = "user_not_exist"
    keyword = "Test"
    self.assertFalse(
      Person.objects.filter(
        user_account = user_account
      ).exists()
    )
    message_count_before = Message.objects.count()
    result = create_Keyword(user_account, keyword,)
    self.assertEqual(result, 400) 
    self.assertEqual(Message.objects.count(), message_count_before,)

  def test_keyword_content(self):
    '''
    keyword內容是不是正確
    '''
    user_account = "test_user_001"
    keyword = "Test"
    # 先取得Person，再用Person查Message
    person = Person.objects.create(user_account=user_account, created_at="2026-03-12") 

    result = create_Keyword(user_account, keyword,)
    self.assertEqual(result, 200) 

    msg = Message.objects.get(user_account=person, keyword=keyword,) 
    self.assertEqual(msg.keyword, keyword) 
    self.assertEqual(msg.user_account, person)