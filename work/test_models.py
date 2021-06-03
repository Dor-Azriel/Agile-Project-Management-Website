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

User = get_user_model()
class UserTest(TestCase):

    def setUp(self):
        user_a = User(username='joe', email='joe@gmail.com')
        user_a_pw = 'something123'
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password('something123')
        user_a.set_password(user_a_pw)
        self.user_a = user_a



    def test_user_exists(self):
        user_count =User.objects.all().count()
        self.assertEqual(user_count,1)
        print(user_count)

    def test_user_password(self):
        #user_qs = User.objects.filter(username_iexact="joe")
       # user_exists = user_qs.exists() and user_qs.count() == 1
        self.assertTrue(
            self.user_a.check_password("something123")
        )
    def test_login_url(self):
        login_url = "/login/"
        data = {"username": "joe", "password": "something123"}
        response = self.client.post(login_url, data, follow=True)

        status_code = response.status_code
        #redirect_path = response.request.get("PATH_INFO")
        # self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(status_code, 200)









