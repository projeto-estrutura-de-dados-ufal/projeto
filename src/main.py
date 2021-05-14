from StaticList import StaticList
from readData import readData


if __name__ == "__main__":
    
    airbnbList = readData()
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

