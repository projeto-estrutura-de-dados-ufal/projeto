import pandas as pd
import random

def readData(path):
    airbnb = pd.read_csv(path).to_dict()


    matrix = []
    for i in airbnb:
        listValues = list(airbnb[i].values())
        matrix.append(listValues)

    allKeys = list(airbnb.keys())
    myList = [] 
    counter = 0
    while counter < len(matrix[0]):
        tempList = {} 
        for i in range(len(matrix)):
            tempList[allKeys[i]] = matrix[i][counter]

        myList.append(tempList)
        counter += 1
        
    hundredElements =[]
    for i in range(100):
        element = random.choice(myList)
        while (element in hundredElements):
            element = random.choice(myList)

        hundredElements.append(element) 

    return hundredElements 