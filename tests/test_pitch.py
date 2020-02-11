import unittest
from app.models import User, Pitch, Comment
from app import db

class PitchModelTest(unittest.TestCase):
    """
    Test Case to test functionality of User Model
    """

    def setUp(self):
        """
        setUp method initializes all our objects before tests
        """
        self.new_user = User(username = 'test_user45', email = "user45@mail.com", password = '1234')
        self.new_pitch = Pitch(category = "Job", content = "The Pitch", user = self.new_user)

    def test_save_pitch(self):
        """
        test_save_pitch method to test if save_pitch methods save pitch object to database
        """
        self.pitch_save_id = self.new_pitch.save_pitch()
        self.assertTrue(self.pitch_save_id)
