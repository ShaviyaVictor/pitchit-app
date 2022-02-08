from click import password_option
from flask_wtf import FlaskForm


from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Length, Email

class logInForm(FlaskForm) :
  username = StringField('username', validators=[InputRequired(), Length(min = 4, max = 15)])
  password = PasswordField('password', validators=[InputRequired(), Length(min = 8, max = 80)])
  remember = BooleanField('Remember me')



class signUpForm(FlaskForm) :
  first_name = StringField('first name', validators=[InputRequired(), Length(min=4, max=15)])
  last_name = StringField('last name', validators=[InputRequired(), Length(min=4, max=15)])
  username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
  email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(min=4, max=20)])
  password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)])



class pitchForm(FlaskForm) :
  pitch = StringField('pitch', widget=Textarea(), validators=[InputRequired()])