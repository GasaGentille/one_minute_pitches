from app.models import Comment,User,Pitch
from app import db
import unittest

class PitchModelTest(unittest.TestCase):

    def setUp(self):
            self.new_user = User(username = 'James',password = 'potato', email = 'james@ms.com')
            self.new_pitch = Pitch(id=12345,pitch_title='Test',pitch_content='Pitches test',category='competitor', user = self.user_James, upvotes=0, downvotes =0)

    def tearDown(self):
            Pitch.query.delete()
            User.query.delete()

    def test_check_instance_variables(self):
            self.assertEquals(self.new_pitch.pitch_id,12345)
            self.assertEquals(self.new_pitch.pitch_title,'Test')
            self.assertEquals(self.new_pitch.pitch_content,'Pitches test')
            self.assertEquals(self.new_pitch.category,'competitor')
            self.assertEquals(self.new_pitch.user,self.user_James)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):

            self.new_pitch.save_pitch()
            got_pitch = Pitch.get_pitch(12345)
            self.assertTrue(len(got_pitch is not None)