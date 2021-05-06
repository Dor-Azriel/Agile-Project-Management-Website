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

    def test_is_upper(self):
        tmp = skill.objects.create(level="JU", language="JA")
        self.assertEqual(tmp.is_upperclass(),"JAJU")

    def test_str(self):
        tmp = skill.objects.create(level="JU", language="JA")
        self.assertEqual(tmp.__str__(),"JAJU")

class TestTask(TestCase):
    def test_init(self):
        self.tmp=Task.objects.create(startTime=datetime(2020,4,4)
                                     ,endTime=datetime(2020,4,5)
                                     ,inCharge=User.objects.get(pk=1)
                                     ,lastUpdate=datetime(2020,4,4)
                                     ,cost=1000
                                     , subTasks=SubTask.objects.get(pk=1),
                                     TaskName="Test"
                                     ,Description="testing")
    def test_incharge(self):
        tmp = Task.objects.create(startTime=datetime(2020, 4, 4)
                                  , endTime=datetime(2020, 4, 5)
                                  , inCharge=User.objects.get(pk=1)
                                  , lastUpdate=datetime(2020, 4, 4)
                                  , cost=1000
                                  , subTasks=SubTask.objects.get(pk=1),
                                  TaskName="Test"
                                  , Description="testing")
        self.assertEqual(User.objects.get(pk=1),tmp.inCharge)

    def test_subTask(self):
        tmp = Task.objects.create(startTime=datetime(2020, 4, 4)
                                  , endTime=datetime(2020, 4, 5)
                                  , inCharge=User.objects.get(pk=1)
                                  , lastUpdate=datetime(2020, 4, 4)
                                  , cost=1000
                                  , subTasks=SubTask.objects.get(pk=1),
                                  TaskName="Test"
                                  , Description="testing")
        self.assertEqual(SubTask.objects.get(pk=1), tmp.subTasks)

class Testreview(TestCase):
    def test_init(self):
        self.new=review.objects.create(ProjectName="TEST",Description="TEST"
                                       ,TaskReview=Task.objects.get(pk=1))

# class TestSprint(TestCase):
#     def test_init(self):

