from unittest import TestCase
from work.models import skill
from work.models import review
from work.models import Task
from datetime import datetime
from django.contrib.auth.models import User
from work.models import SubTask

class Testskill(TestCase):

    def test_init(self):
        self.tmp = skill.objects.create(level="JU",language="JA")

    def test_is_equal(self):
        tmp = skill.objects.create(level="JU", language="JA")
        self.assertEqual(tmp.level,"JU")
        self.assertEqual(tmp.language, "JA")

class TestTask(TestCase):
    def test_init(self):
        self.tmp=Task.objects.create(startTime=datetime(2020,4,4)
                                     ,endTime=datetime(2020,4,5)
                                     ,inCharge=User.objects.get(pk=1)
                                     ,lastUpdate=datetime.now()
                                     ,cost=1000
                                     , subTasks=SubTask.objects.get(pk=1),
                                     TaskName="Test"
                                     ,Description="testing")

class Testreview(TestCase):
    def test_init(self):
        self.new=review.objects.create(ProjectName="TEST",Description="TEST"
                                       ,TaskReview=Task.objects.get(pk=1))
