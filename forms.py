from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired, Required, Optional

class InputForm(FlaskForm):
    #Meat
    fish = BooleanField("Fish", default=False, validators=[Optional()])
    chicken = BooleanField("Chicken", default=False, validators=[Optional()])
    beef = BooleanField("Beef", default=False, validators=[Optional()])
    egg = BooleanField("Egg", default=False, validators=[Optional()])
    #Carbs
    rice = BooleanField("Rice", default=False, validators=[Optional()])
    pasta = BooleanField("Pasta", default=False, validators=[Optional()])
    bread = BooleanField("Bread", default=False, validators=[Optional()])
    #Dairy
    milk = BooleanField("Milk", default=False, validators=[Optional()])
    cheese = BooleanField("Cheese", default=False, validators=[Optional()])
    butter = BooleanField("Butter", default=False, validators=[Optional()])
    #Vegetable
    potato = BooleanField("Potato", default=False, validators=[Optional()])
    carrot = BooleanField("Carrot", default=False, validators=[Optional()])
    garlic = BooleanField("Garlic", default=False, validators=[Optional()])
    onion = BooleanField("Onion", default=False, validators=[Optional()])
    #other
    fruit = BooleanField("Fruit", default=False, validators=[Optional()])

    submit = SubmitField('Find Recipe')

class JSONButton(FlaskForm):
    download = SubmitField('Export as JSON')
