from avltree import Node
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from helpers import readData

from env import env

if __name__ == "__main__":
    airbnbList = readData(env['path_airbnb'])
    myTree = Node(0)
    for i in range(10):
        myTree.insert(airbnbList[i])
            

    myTree.PrintTree()
    print('\n')
    
"""
             3831
    2595              5178
2539   3647      5099      5203
              5022  5121      5238
"""