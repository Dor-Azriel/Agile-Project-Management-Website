from unittest import TestCase
from polls.models import Question
from datetime import datetime
class TestQuestion(TestCase):
    def test_was_published_recently(self):
        tmp =Question.objects.create(question_text="Test",pub_date=datetime(2020, 4, 4))
        #tmp.was_published_recently()
