from work.models import skill

from django.contrib.auth.models import User

from django.test import TestCase


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

    def test_inituser(self):
        self.user = User.objects.create(username='Admin1', email='joe@gmail.com', is_staff=True, is_superuser=True,
                                        password='something123')

    def test_user_1(self):
        user = User.objects.create(username='Admin1', email='joe@gmail.com', is_staff=True, is_superuser=True,
                                   password='something123')
        self.assertEqual(user.username, 'Admin1')

    def test_user_2(self):
        user = User.objects.create(username='Admin1', email='joe@gmail.com', is_staff=True, is_superuser=True,
                                  password='something123')
        self.assertEqual(user.email, 'joe@gmail.com')

    def test_user_3(self):
        user = User.objects.create(username='Admin1', email='joe@gmail.com', is_staff=True, is_superuser=True,
                                  password='something123')
        self.assertEqual(user.password, 'something123')

    def test_user_4(self):
        user = User.objects.create(username='Admin1', email='joe@gmail.com', is_staff=True, is_superuser=True,
                                  password='something123')
        self.assertTrue(user.is_staff)

    def test_user_5(self):
        user = User.objects.create(username='Admin1', email='joe@gmail.com', is_staff=True, is_superuser=True,
                                  password='something123')
        self.assertTrue(user.is_superuser)

    def test_user_6(self):
        user = User.objects.create(username='Admin1', email='joe@gmail.com', is_staff=True, is_superuser=True,
                                  password='something123', is_active=True)
        self.assertTrue(user.is_active)





