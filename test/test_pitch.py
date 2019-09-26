from app.models import Comment,User,Pitch
from app import db
import unittest

class PitchModelTest(unittest.TestCase):

        def setUp(self):
                self.new_user = User(id=1, username = 'James',password = 'potato', email = 'james@ms.com')
                self.new_pitch = Pitch(id=12349,user_id=self.new_user.id, pitch_title='Test',pitch_content='Pitches test',category='competitor', upvotes=0, downvotes =0)



        def test_check_instance_variables(self):
                self.assertEquals(self.new_pitch.id,12349)
                self.assertEquals(self.new_pitch.pitch_title,'Test')
                self.assertEquals(self.new_pitch.pitch_content,'Pitches test')
                self.assertEquals(self.new_pitch.category,'competitor')
                self.assertEquals(self.new_pitch.user_id,self.new_user.id)

        def test_save_pitch(self):
                self.new_pitch.save_pitch()
                self.assertTrue(len(Pitch.query.all())>0)

      