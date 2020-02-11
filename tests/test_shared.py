import unittest
from app.models import User, Comment, Pitch
from app import db

class SharedModelTest(unittest.TestCase):
    """
    Test Case to test functionality of User Model
    """

    def setUp(self):
        """
        setUp method initializes all our objects before tests
        """
        self.new_user = User(username = 'test_user', email = "user@mail.com", password = '1234')
        self.new_pitch = Pitch(category = "Job", content = "The Pitch", user_id = self.new_user.user_id)
        self.new_comment = Comment(content = "A comment", pitch_id = self.new_pitch.pitch_id, user_id = self.new_user.user_id)

    def test_user_instance(self):
        """
        test_instance test case to test if new_user is of instance User
        """
        self.assertTrue(isinstance(self.new_user, User))

    def test_pitch_instance(self):
        """
        test_instance test case to test if new_user is of instance User
        """
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_comment_instance(self):
        """
        test_instance test case to test if new_user is of instance User
        """
        self.assertTrue(isinstance(self.new_comment, Comment))
