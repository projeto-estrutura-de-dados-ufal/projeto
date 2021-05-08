import pandas as pd

def readData():
    airbnb = pd.read_csv('../data/airbnb.csv').to_dict()

    matrix = []
    for i in airbnb:
        listValues = list(airbnb[i].values())
        matrix.append(listValues)

    allKeys = list(airbnb.keys())
    myDict = {} 
    counter = 0
    while counter < len(matrix[0]):
        tempList = {} 
        j = 0
        for i in range(len(matrix)):
            if j != 0:
                tempList[allKeys[i]] = matrix[i][counter]
            j += 1

        myDict[matrix[0][counter]] = tempList
        counter += 1
        
    return myDict

        
if __name__ == "__main__":
    myDict = readData()
    for i in myDict:
        print(i, myDict[i])
