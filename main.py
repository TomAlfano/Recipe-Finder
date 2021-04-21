from flask import Flask, render_template, request
from .forms import  InputForm

import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = 'f5f35514a2e828fe0c328b21391b80ec273fcf680c98b1f3'


url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "<YOUR_RAPID_API_KEY>",
  }

def numberize(checkBoxInput):
    if checkBoxInput == False:
        return 0
    else:
        return 1

@app.route('/', methods=['GET', 'POST'])
def search_page():
    form = InputForm()
    if form.validate_on_submit():
        ingredientInput = [{'meat':numberize(form.meat.data)},{'fish':numberize(form.fish.data)},
            {'vegetable':numberize(form.vegetable.data)},{'fruit':numberize(form.fruit.data)},{'pasta':numberize(form.pasta.data)},
            {'rice':numberize(form.rice.data)},{'egg':numberize(form.egg.data)},{'dairy':numberize(form.dairy.data)},
            {'pizza':numberize(form.pizza.data)}]
        return redirect('/results')
    return render_template('website.html', form=form)

@app.route("/results", methods=['GET', 'POST'])
def result():
    return renter_template('results.html')

if __name__ == '__main__':
  app.run()
