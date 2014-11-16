# pylint: disable=unexpected-keyword-arg, no-value-for-parameter
"""This is the test suite"""
from django.test import TestCase
from django.utils import timezone
from frontend.models import Post

# Create your tests here.

class ModelTests(TestCase):
    # pylint: disable=R0904
    """ Test all the models"""
    def test_model_(self):
        """ Does the model save/load? """
        testpost = Post(title="TestCase01", body="SOUND", pub_date=timezone.now(), user="Tester", likes=5)
        testpost.save()
        callpost = Post.objects.get(id=1)
        self.assertEqual(callpost.title, "TestCase01")
        self.assertEqual(callpost.user, "Tester")
        self.assertEqual(callpost.likes, 5)
