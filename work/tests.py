from work.models import skill
from work.models import review
from work.models import Task
from datetime import datetime
from django.contrib.auth.models import User
from work.models import SubTask
from work.models import Sprint
from work.models import Conclusions
from work.models import project
from work.models import review
from django.urls import resolve, reverse
from django.test import TestCase, tag
from django.core.files import File
from django.contrib.auth import get_user_model
from django.conf import settings
#from mysite import urls, settings
from pages import views

class Testskill(TestCase):

    def test_init(self):
        self.tmp = skill.objects.create(level="JU", language="JA")

    def test_is_equal(self):
        tmp = skill.objects.create(level="JU", language="JA")
        self.assertEqual(tmp.level, "JU")
        self.assertEqual(tmp.language, "JA")

    def test_is_upper(self):
        tmp = skill.objects.create(level="JU", language="JA")
        self.assertEqual(tmp.is_upperclass(), "JAJU")

    def test_str(self):
        tmp = skill.objects.create(level="JU", language="JA")
        self.assertEqual(tmp.__str__(), "JAJU")


class Test_Model_User(TestCase):

    def setup(self):
        self.user = User.objects.create(username='Admin1', email='joe@gmail.com', is_staff=True, is_superuser=True,
                                        password='something123')

    def testUSER(self):
        user = User.objects.create(username='Admin1', email='joe@gmail.com', is_staff=True, is_superuser=True,
                                   password='something123')
        self.assertEqual(user.username, 'Admin1')