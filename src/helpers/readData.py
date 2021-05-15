import pandas as pd
from env import env

def readData():
    airbnb = pd.read_csv(env['path']).to_dict()

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
        
    return myList 