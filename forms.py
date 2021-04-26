from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired, Required, Optional

locations = [('en','England'), ('fr','France'), ('ca','Canada'), ('me','Middle East'), ('ru','Russia'), ('ch','China')]

class InputForm(FlaskForm):
    cvlist = ['Meat', 'Vegetable', 'Pasta', 'Rice','Fruit','Egg','Dairy','Pizza','Fish']
    meat = BooleanField("Meat", default=False, validators=[Optional()])
    vegetable = BooleanField("Vegetable", default=False, validators=[Optional()])
    pasta = BooleanField("Pasta", default=False, validators=[Optional()])
    rice = BooleanField("Rice", default=False, validators=[Optional()])
    fruit = BooleanField("Fruit", default=False, validators=[Optional()])
    pizza = BooleanField("Pizza", default=False, validators=[Optional()])
    egg = BooleanField("Egg", default=False, validators=[Optional()])
    dairy = BooleanField("Dairy", default=False, validators=[Optional()])
    fish = BooleanField("Fish", default=False, validators=[Optional()])

    location = SelectField(u'Location', choices = locations)
    #ingredients = SelectMultipleField(u'Ingredient', choices = cvlist,  validators=[InputRequired()])
    submit = SubmitField('Find Recipe')
