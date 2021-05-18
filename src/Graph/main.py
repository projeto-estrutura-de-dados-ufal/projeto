from Graph import Graph
import pandas as pd
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from helpers import readData

if __name__ == "__main__":
    heroi = pd.read_csv('../../data/hero-network.csv')

    heroi1 = heroi["hero1"]
    heroi2 = heroi["hero2"]


    size = 10
    herois = []
    for i in range(size):
        # print(heroi1[i], " --> ", heroi2[i])
        if (heroi1[i] not in herois):
            herois.append(heroi1[i])

    for j in range(size):
        if (heroi2[j] not in herois):
            herois.append(heroi2[j])

        
    myGraph = Graph(size)
    for i in herois:
        myGraph.add_node(i)

    print("\n\n\n")
    myGraph.print_nodes()

    for i in range(size):
        v1 = myGraph.get_index(heroi1[i])
        v2 = myGraph.get_index(heroi2[i])
        myGraph.add_edge(v1, v2)
    
    print("\n\n\n")
    myGraph.print_graph()
    # myGraph.remove_node("LITTLE, ABNER")
    myGraph.add_node("capitao, brazuca")
    myIndex = myGraph.get_index("capitao, brazuca")
    myGraph.add_edge(myIndex,0)
    myGraph.print_graph()





#[cap america][homem de ferro]=1
#matrix[Littleabner][0] = princess zanda
#matrix[Littleabner][1] = pantera negra

#                 littleabner | princess | pantera
# littleabner |        0           1          1
# princess    |
# pantera     |




#para não ler repetidos é possivel utilizar o  "if i not in heroi :   herois[]"






