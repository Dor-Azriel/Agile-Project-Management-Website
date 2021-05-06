from unittest import TestCase
from work.models import skill


class Testskill(TestCase):
    def test_is_upperclass(self):
        self.tmp = skill.objects.create(language="JA", level="JU")
        self.assertEqual(str(self.tmp.language),"JA")
