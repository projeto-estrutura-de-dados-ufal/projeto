import pandas as pd

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
        
    return myList 