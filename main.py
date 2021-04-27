#importing of libraries
from flask import Flask, render_template, request, url_for, redirect
from .cvsetup import  InputForm, JSONButton
from .bayes import machineLearning
import json
import requests

#flask setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ShhItsASecret'

#api setup
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "88a64d9efdmsh2e4be6f10fa1609p17a7dcjsn6b18e14d8cee",
  }

#sets global variable for SQL work-around
global ingredientInput
ingredientInput = 'Please click "Find Recipe"'
global response
response = ""
global machineCountry
machineCountry = {}


#changes checkbox input from True/False to 1/0
def numberize(checkBoxInput):
    if checkBoxInput == False:
        return 0
    else:
        return 1

#landing page
@app.route('/', methods=['GET', 'POST'])
def search_page():
    form = InputForm() #converting the forms present in forms.py to a variable in order to perform python operations on them
    button = JSONButton()
    if form.validate_on_submit():
        OutputString = ""
        querystring = ""
        global ingredientInput
        ingredientInput =  {'fish':numberize(form.fish.data),'chicken':numberize(form.chicken.data),'beef':numberize(form.beef.data),'egg':numberize(form.egg.data),'rice':numberize(form.rice.data),'pasta':numberize(form.pasta.data),'bread':numberize(form.bread.data),'milk':numberize(form.milk.data),'cheese':numberize(form.cheese.data),'butter':numberize(form.butter.data),'potato':numberize(form.potato.data),'carrot':numberize(form.carrot.data),'garlic':numberize(form.garlic.data),'onion':numberize(form.onion.data),'fruit':numberize(form.fruit.data)} #checks the values of the form
        inputCheckboxes = []
        for ingredient, value in ingredientInput.items():
            inputCheckboxes.append(value)
            if value == 1:
                OutputString = OutputString + " " + ingredient #creates a string to query the api with, with selected ingredients being seperated by a space
        global machineCountry
        machineCountry = machineLearning(inputCheckboxes) #runs the machinelearning function to determine the most likely cuisine that the selected ingredients correspond to
        querystring = {"query":OutputString,"number":"5","offset":"0","instructionsRequired":"true","cuisine":machineCountry} #the value that is queried to the api
        global response
        response = requests.request("GET", url, headers=headers, params=querystring).json() #the response from the api converted into json format
        if response !=None:
            if button.validate_on_submit(): #if button is clicked, saves a json and html file with the result of the api query
                with open('dump.json', 'w') as json_file:
                    json.dump(response, json_file)
                with open('dump.html', 'w') as json_file:
                    json.dump(response, json_file)
        return redirect(url_for('search_page', value=ingredientInput, form=form, button=button, machineCountry=machineCountry, response=response))
    return render_template('website.html', title="Popty" , form=form, button=button, value=ingredientInput, response=response, machineCountry=machineCountry)

if __name__ == '__main__':
  app.run()
