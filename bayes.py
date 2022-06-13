#DISCLAIMER: been a while since I programmed this so I've done these comments to the best of my knowlegde

#inputCheckboxes is the input from the flask form on the page. This is used to calculate the similarity.
def machineLearning(inputCheckboxes):
    import csv
    import math
    with open(r'data.csv', newline ='') as csvfile:
        data=list(csv.reader(csvfile))
        c=0
        separated=[]
        trainingDict = {'Italian':[],'Mexican':[],'Indian':[],'French':[],'British':[],'Japanese':[]}
        #puts data into dictionary of arrays, including dish name
        for row in data:
            separated.append(row)
            #Starts by sorting separating out the rows of training data by class, cusine country here
            if row[(len(row)-1)]== 'Italian':
                trainingDict['Italian'].append(row)
            elif row[(len(row)-1)]== 'Mexican':
                trainingDict['Mexican'].append(row)
            elif row[(len(row)-1)]== 'Indian':
                trainingDict['Indian'].append(row)
            elif row[(len(row)-1)]== 'British':
                trainingDict['British'].append(row)
            elif row[(len(row)-1)]== 'French':
                trainingDict['French'].append(row)
            elif row[(len(row)-1)]== 'Japanese':
                trainingDict['Japanese'].append(row)
            #counts the total amount of entries of training data, used in final calculation
            c=c+1

        sumTrainingData = c
        #totals cv for training data for each class
        #loops through the dict containing training data sorted into their separate classes
        for key in trainingDict:
            totalList = []
            c=0
            #loops though each row of training data arrays attached to dictionary item
            for row in trainingDict[key]:
                #starts at one due to 0 column containing the name of the dish which we don't need to calculate the probability
                i=1
                #len -1 due to final entry being the cusine country
                #loops through each item in array within the current training dict arrays
                while i<(len(row)-1):
                    #catches the first loop so that a datapoint for each item on the cv exists so they can be changed
                    if c == 0:
                        if row[i] == '1':
                            totalList.append(1)
                        else:
                            totalList.append(0)
                    else:
                        #once the first loop is done it loops through the rest of the meals with the same class
                        #it then totals the amount of dishes containing that ingredient by adding the what was there when a 1 is found
                        if row[i] == '1':
                            totalList[(i-1)]=(totalList[(i-1)]+1)
                        else:
                            totalList[(i-1)]=(totalList[(i-1)])
                    i=i+1
                c=c+1
            #Adds the array containing the total amound of recipies with those ingredients to the end of the array under the correct dict item
            trainingDict[key].append(totalList)

        finalProbability = 0
        probability = 0
        #Start of calculating the probabilities of each dish
        #loops through each item in dict by key
        for key in trainingDict:
            probabilityScores = []
            compareArray = []
            #sets the compare array the the previously calculated and apended array totalList for the correct class
            compareArray = trainingDict[key][(len(trainingDict[key])-1)]
            i=0
            #sets up the array containing the probabilities of that ingredient being from a country
            while i < len(inputCheckboxes):
                #if input is a checked box then 'yes' so simply amount of 'yeses' divided by the total items in that class
                if inputCheckboxes[i] == 1:
                    probabilityScores.append((compareArray[i]/(len(trainingDict[key]))))
                #same as previous one but for 'no' from the form so 1- the equation above
                else:
                    probabilityScores.append(1-(compareArray[i]/(len(trainingDict[key]))))

                i=i+1
            #puts first probability into the the probability variable
            probability = probabilityScores[0]
            i=1
            #loops through all the probabilities just calculated in probabilityScores
            while i < len(inputCheckboxes):
                #when multiplying a list of numbers the order doesn't matter so it simply overwrites the previous number by multiplying by the next probability in the array
                probability = probability*probabilityScores[i]
                i=i+1
            #sets up return variable in right format
            #only stores the probability that is the highest. If a later probability is greater it will overwrite
            #--------------------------------------------- Error I think is here where I miss out sumTrainingData in the final probability
            #probability = sumTrainingData * probability           EXAMPLE, ERROR MIGHT BE HERE
            if finalProbability < probability:
                finalProbability = probability * sumTrainingData
                #key is the cousine country calculated to be most similar too. This is kept for further processing later
                fProbability = { key : probability }
        #returns probability to main
        return fProbability
