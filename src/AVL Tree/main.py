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
            

    myTree.remove(2539)
    myTree.remove(3647)
    myTree.PrintTree()
    print('\n')
    
"""
             3831
    2595              5178
2539   3647      5099      5203
              5022  5121      5238
"""
"""
Removendo a raiz original:
             3647 
    2595              5178
2539             5099      5203
              5022  5121      5238
"""
"""
Mantendo a raiz original e removendo 2539
             3831
    2595              5178
        3647     5099      5203
              5022  5121      5238
"""
"""
Não removendo a raiz original e removendo 2539 e 3647
           5099
    3831          5178
2595   5022    5121  5203
                        5238
"""