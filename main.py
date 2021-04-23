from flask import Flask, render_template, request, url_for, redirect
from .forms import  InputForm, locations

import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ShhItsASecret'

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "<YOUR_RAPID_API_KEY>",
  }

#sets global variable for SQL work-around
global ingredientInput
ingredientInput = 'Please click "Find Recipe"'

#changes checkbox input from True/False to 1/0
def numberize(checkBoxInput):
    if checkBoxInput == False:
        return 0
    else:
        return 1

#landing page
@app.route('/', methods=['GET', 'POST'])
def search_page():
    form = InputForm()
    #message = 'Please click "Find Recipe"'
    if form.validate_on_submit():
        global ingredientInput
        ingredientInput = {'country':dict(locations).get(form.location.data),'meat':numberize(form.meat.data),'fish':numberize(form.fish.data),'vegetable':numberize(form.vegetable.data),'fruit':numberize(form.fruit.data),'pasta':numberize(form.pasta.data),'rice':numberize(form.rice.data),'egg':numberize(form.egg.data),'dairy':numberize(form.dairy.data),'pizza':numberize(form.pizza.data)}
        return redirect(url_for('search_page', value=ingredientInput, form=form))
    return render_template('website.html', title="Popty" , form=form, value=ingredientInput)

if __name__ == '__main__':
  app.run()
