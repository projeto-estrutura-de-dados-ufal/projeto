from Stack import Stack
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from helpers import readData


from helpers import readData

if __name__ == "__main__":
    
    airbnbList = readData()
    myStack = Stack()
    # [1, 2, 3, 4]
    # myStack.myList = airbnbList
    for i in range(myStack.limit):
        myStack.insert(airbnbList[i])

    
 
    myStack.search(5022)
    #myStack.show()
    #myStack.tam()
    #myStack.remove()

    #print(myStack.binarySearch(2539))
    #myStack.tam()
