
from django.urls import reverse
from django.test import TestCase


class TestVIEW(TestCase):

    def test_Devlop_home_views(self):
        response = self.client.get(reverse('DevlopHome_views'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_tasks_home_views(self):
        response = self.client.get(reverse('tasks_views'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_logd_view_home_views(self):
        response = self.client.get(reverse('logd_view'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_home_view_home_views(self):
        response = self.client.get(reverse('home_view'), follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)





