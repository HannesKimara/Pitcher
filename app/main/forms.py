from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    category = SelectField('Category', choices = [('General', 'General'), ('Promotion','Promotion'), ('Interview','Interview'), ('Product','Product')],validators=[Required()])
    content = StringField('Your Pitch :', validators = [Required()])
    submit = SubmitField('submit')

class CommentForm(FlaskForm):
    content = StringField('Comment', validators = [Required()])
    submit = SubmitField('submit')