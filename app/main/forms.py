from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch title',validators = [Required()])
    text = TextAreaField('Text',validators = [Required()])
    category = SelectField('Type',choices = [('competitor','Competitor pitch'),('employee','Employee pitch'),('sport','Sport pitch')], validators = [Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
   bio = TextAreaField('Tell us about you.',validators = [Required()])
   submit = SubmitField('Submit')
# class ReviewForm(FlaskForm):
#    title = StringField('Review title',validators=[Required()])
#    review = TextAreaField('Movie review', validators=[Required()])
#    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators = [Required()])
    submit = SubmitField('Submit')
