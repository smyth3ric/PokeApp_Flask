from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SearchField
from wtforms.validators import DataRequired, EqualTo



class UserCreationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

class UserLoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PokeForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()],)
    submit = SubmitField('catch-em-all')


