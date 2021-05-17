from StaticList import StaticList
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from env import env
from helpers import readData

if __name__ == "__main__":
    airbnbList = readData(env['path_airbnb'])
    myStaticList = StaticList()
    # [1, 2, 3, 4]
    # myStaticList.myList = airbnbList
    
    for i in range(myStaticList.limit):
        myStaticList.insertOrdered(airbnbList[i])

    
    myStaticList.show()
    myStaticList.tam()
    #myStaticList.search()
    myStaticList.remove(2539)
    myStaticList.tam()
    print(myStaticList.binarySearch(2539))
    #myStaticList.tam()

