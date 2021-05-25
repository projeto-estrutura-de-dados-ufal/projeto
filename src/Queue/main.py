from Queue import Queue 
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from helpers import readData

from env import env

if __name__ == "__main__":
    
    airbnbList = readData(env['path_airbnb'])

    myQueue = Queue()
    for i in range(myQueue.limit):
        myQueue.insert(airbnbList[i])

    myQueue.show()
    #myQueue.remove()
    print("##############################################################################################################################")
    myQueue.tam()
    myQueue.remove()
    print("##############################################################################################################################")
    myQueue.insert(airbnbList[0])
    myQueue.show()