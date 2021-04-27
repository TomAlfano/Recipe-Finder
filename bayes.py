
def machineLearning(inputCheckboxes):
    import csv
    import math
    with open(r'data.csv', newline ='') as csvfile:
        data=list(csv.reader(csvfile))
        c=0
        separated=[]
        trainingDict = {'Italian':[],'Mexican':[],'Indian':[],'French':[],'British':[],'Japanese':[]}
        #puts data into rows, including dish name
        for row in data:
            separated.append(row)
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
            c=c+1

        sumTrainingData = c
        #totals cv for training data for each class
        for key in trainingDict:
            totalList = []
            c=0
            for row in trainingDict[key]:

                i=1
                while i<(len(row)-1):
                    if c == 0:
                        if row[i] == '1':
                            totalList.append(1)
                        else:
                            totalList.append(0)
                    else:
                        if row[i] == '1':
                            totalList[(i-1)]=(totalList[(i-1)]+1)
                        else:
                            totalList[(i-1)]=(totalList[(i-1)])
                    i=i+1
                c=c+1
            #Only totals yeses in array in totalList
            trainingDict[key].append(totalList)

        finalProbability = 0
        probability = 0
        for key in trainingDict:
            probabilityScores = []
            compareArray = []
            compareArray = trainingDict[key][(len(trainingDict[key])-1)]
            i=0
            while i < len(inputCheckboxes):
                if inputCheckboxes[i] == 1:
                    probabilityScores.append((compareArray[i]/(len(trainingDict[key]))))
                else:
                    probabilityScores.append(1-(compareArray[i]/(len(trainingDict[key]))))

                i=i+1
            probability = probabilityScores[0]
            i=1
            while i < len(inputCheckboxes):
                probability = probability*probabilityScores[i]
                i=i+1
            #sets up return variable in right format
            if finalProbability < probability:
                finalProbability = probability
                fProbability = { key : probability }
        return fProbability
