from django.test import TestCase

# Create your tests here.
from work.models import skill


class TestModels(TestCase):
    def user_create(self):
        self.tmp=skill.objects.create(language="JA",level="JU")
       # self.assertEqual(str(lang),"JAVA")