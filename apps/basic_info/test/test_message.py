from django.test import TestCase
from apps.basic_info.models import Person,Message
from apps.basic_info.services.actions import create_Keyword

class MessageModelTests(TestCase):
  '''
  測試key word message
  '''
  def test_message_model_exists(self):
    msg = Message.objects.count()
    self.assertEqual(msg,0)

  def test_create_Keyword_when_user_exists(self):
    '''
    user存在->message可以建立
    '''
    Person.objects.create(
      user_account = "test_user_001", 
      created_at = "2026-03-12"
    )
    keyword = "Test"
    person = Person.objects.get(user_account = "test_user_001")

    result = create_Keyword(person.user_account,keyword)
    self.assertEqual(result, True)
    self.assertTrue(
      Message.objects.filter(user_account = person).exists()
    )


  def test_cannot_create_keyword_when_user_not_exists(self):
    '''
    user不存在->不能insert到message
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
    self.assertEqual(result, False) 
    self.assertEqual(Message.objects.count(), message_count_before,)

  def test_keyword_content(self):
    '''
    keyword內容是不是正確
    '''
    user_account = "test_user_001"
    keyword = "Test"
    # 先取得Person，再用Person查Message
    person = Person.objects.create(
      user_account=user_account, 
      created_at="2026-03-12"
    ) 

    result = create_Keyword(user_account, keyword,)
    self.assertEqual(result, True) 

    msg = Message.objects.get(user_account=person, keyword=keyword,) 
    self.assertEqual(msg.keyword, keyword) 
    self.assertEqual(msg.user_account, person)