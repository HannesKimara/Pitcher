import unittest
from app.models import User, Pitch, Comment
from app import db

class CommentModelTest(unittest.TestCase):
    """
    Test Case to test functionality of Comment Model
    """

    def setUp(self):
        """
        setUp method initializes all our objects before tests
        """
        self.new_user = User(username = 'test_user12', email = "user12@mail.com", password = '1234')
        self.new_pitch = Pitch(category = "Job", content = "The Pitch", user = self.new_user)
        self.new_comment = Comment(content = "A comment", pitch_id = self.new_pitch.pitch_id, user_id = self.new_user.user_id)

    def test_save_comment(self):
        """
        test_save_comment method to test if save_comment method works
        """
        self.comment_save_id = self.new_comment.save_comment()
        self.assertTrue(self.comment_save_id)
