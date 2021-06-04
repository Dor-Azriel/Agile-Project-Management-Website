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




class ClientTest(TestCase):

    def setUp(self):
        user_d = User(username='Client', email='Developer@gmail.com')
        user_d_gr = 'Client'
        user_d.is_staff = False
        user_d.is_superuser = False
        user_d.is_active = True
        user_d.get_group_permissions(user_d_gr)
        user_d.save()
        user_d.set_password('something123')
        self.user_d = user_d


    def test_client_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        print(user_count)

    def test_client_password(self):
        self.assertTrue(
            self.user_d.check_password("something123")
        )

    def test_client_login_logout_url(self):
        login_url = "/login/"
        data = {"username": "Client", "password": "something123"}
        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response = self.client.get(reverse('logout'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)


    def test_client_login_massageview(self):
        login_url = "/login/"
        data = {"username": "Client", "password": "something123"}

        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response = self.client.get(reverse('MessagePage_view'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)






class UserTest(TestCase):

    def setUp(self):
        user_a = User(username='Admin', email='joe@gmail.com')
        user_a_pw = 'something123'
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password('something123')
        user_a.set_password(user_a_pw)
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        print(user_count)

    def test_user_password(self):
        # user_qs = User.objects.filter(username_iexact="joe")
        # user_exists = user_qs.exists() and user_qs.count() == 1
        self.assertTrue(
            self.user_a.check_password("something123")
        )

    def test_login_logout_url(self):
        login_url = "/login/"
        data = {"username": "Admin", "password": "something123"}
        response = self.client.post(login_url, data, follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

        response = self.client.get(reverse('logout'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
    






























