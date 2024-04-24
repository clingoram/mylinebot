from django.test import TestCase
from datetime import datetime

# Create your tests here.
from .models import Person,Message

class PersonModelTests(TestCase):
  def test_perosn_model_exists(self):
    person = Person.objects.count()

    self.assertEqual(person,0)

  # def test_models_has_string(self):
  #   person = Person.objects.create(uid="Ukd545gdf8g7df8g",account = "User",created_at = datetime.now())
  #   self.assertEqual(person,person.uid)