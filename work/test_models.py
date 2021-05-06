from unittest import TestCase
from work.models import skill
from work.models import review
from work.models import Task
from datetime import datetime

class Testskill(TestCase):
    def test_is_upperclass(self):
        self.tmp = skill.objects.create(language="JA", level="JU")

    def is_equal(self):
        TestCase.failUnlessEqual(self.tmp.level, "JU")
        TestCase.failUnlessEqual(self.tmp.language, "JA")
        #TestCase.fail

class TestTask(TestCase):
    def init(self):
        self.tmp=Task.objects.create(startTime=datetime(2020,4,4)
                                     ,endTime=datetime(2020,4,5)
                                     ,inCharge=1,lastUpdate=datetime.now()
                                     ,cost=1000
                                     , subTasks=1,
                                     TaskName="Test"
                                     ,Description="testing")

class Testreview(TestCase):
    def init(self):
        self.new=review.objects.create(ProjectName="TEST",Testreview="TEST",TaskReview=1)
