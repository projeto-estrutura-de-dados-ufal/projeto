import pandas as pd
from StaticList import StaticList

def readData():
    airbnb = pd.read_csv('../data/airbnb-all-elements.csv').to_dict()

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

        
if __name__ == "__main__":
    airbnbList = readData()

    myStaticList = StaticList()

    print("Antes")
    print(myStaticList.myList)
    print(myStaticList.limit)
    print(myStaticList.size)

    for i in range(myStaticList.limit):
        myStaticList.insert(airbnbList[i])

    print("Depois")
    print(myStaticList.myList)
    print(myStaticList.size)