from LinkedList import LinkedList 
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from helpers import readData
from env import env

if __name__ == "__main__":
    
    airbnbList = readData(env['path_airbnb'])
    myLinkedList = LinkedList()

    size = 100
    for i in range(size):
        myLinkedList.insert(airbnbList[i])
    
    myLinkedList.show()
    print("\n\n\n")
    myLinkedList.delete(2595)
    myLinkedList.delete(2539)
    myLinkedList.show()