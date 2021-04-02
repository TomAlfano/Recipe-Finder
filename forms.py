from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired


#THIS IS AN EXAMPLE OF THE BACK-END OF A FORM
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Regexp('^.{4,10}$', message='Your password should be between 4 and 10 characters long.')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
