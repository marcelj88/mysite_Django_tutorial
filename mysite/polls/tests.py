import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question
from django.db.models.lookups import Day
# Create your tests here.

class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
        
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recenlty() should return False for questions whose pub_date
        is older than one Day
        """
        time = timezone.now() - datetime.timedelta(hours=25)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recenlty() should return True for questions whose pub_date
        is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)
            