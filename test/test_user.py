from app.models import User,Pitch,Comment
from app import db
import unittest

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch = Pitch(pitch_title='Test',pitch_content='Pitches test',category='competitor', upvotes=0, downvotes =0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.new_user,pitch=self.new_pitch)

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('potato'))

    # def tearDown(self):
    #     self.new_pitch.query.delete()
    #     self.new_comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.new_user)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
