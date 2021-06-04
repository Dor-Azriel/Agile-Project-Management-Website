from django.test import TestCase, tag
from django.contrib.auth import get_user_model
from work.models import User
from django.urls import  reverse,resolve
from django.http import HttpRequest, HttpResponse
from django.test.client import Client




User = get_user_model()

class MangerTest(TestCase):

    def setUp(self):
        user_b = User(username='Manager', email='joe@gmail.com')
        user_b_pw = 'something123'
        user_b_gr = 'projectManager'
        user_b.is_staff = False
        user_b.is_superuser = False
        user_b.is_active = True
        user_b.get_group_permissions(user_b_gr)
        user_b.save()
        user_b.set_password('something123')
        user_b.set_password(user_b_pw)
        self.user_b = user_b


    def test_manager_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        print(user_count)

    def test_manager_password(self):
        self.assertTrue(
            self.user_b.check_password("something123")
        )

    def test_manager_login_logout_url(self):
        login_url = "/login/"
        data = {"username": "Manager", "password": "something123"}
        response = self.client.post(login_url, data, follow=True)

        status_code = response.status_code
        self.assertEqual(status_code, 200)


        response = self.client.get(reverse('logout'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_manager_login_massageview(self):
        login_url = "/login/"
        data = {"username": "Manager", "password": "something123"}

        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response = self.client.get(reverse('MessagePage_view'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)





class DeveloperTest(TestCase):

    def setUp(self):
        user_c = User(username='Developer', email='Developer@gmail.com')
        user_c_gr = 'Developer'
        user_c.is_staff = False
        user_c.is_superuser = False
        user_c.is_active = True
        user_c.get_group_permissions(user_c_gr)
        user_c.save()
        user_c.set_password('something123')
        self.user_c = user_c



    def test_developer_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        print(user_count)

    def test_developer_password(self):
        self.assertTrue(
            self.user_c.check_password("something123")
        )

    def test_developer_login_logout_url(self):
        login_url = "/login/"
        data = {"username": "Developer", "password": "something123"}
        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response = self.client.get(reverse('logout'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_developer_login_massageview(self):
        login_url = "/login/"
        data = {"username": "Developer", "password": "something123"}

        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response = self.client.get(reverse('MessagePage_view'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)



































