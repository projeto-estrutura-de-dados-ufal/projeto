from Graph import Graph
import pandas as pd

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from env import env

if __name__ == "__main__":
    hero = pd.read_csv(env['path_marvel'])

    hero1 = hero["hero1"]
    hero2 = hero["hero2"]

    myGraph = Graph()
    myGraph.addNode("Little Abner")
    # myGraph.show()
    # print('\n')
    myGraph.addNode("Princess")
    myGraph.addEdge("Little Abner", "Princess")
    myGraph.addEdge("Princess", "Little Abner")
    # myGraph.addEdge("Little Abner", "Princess")
    # myGraph.show()
    # print('\n')
    myGraph.addNode("Homem de Ferro")
    myGraph.addNode("Pantera Negra")
    myGraph.addNode("Homem Aranha")
    # myGraph.show()
    # print('\n')
    myGraph.addNode("Cap.")
    myGraph.addEdge("Homem de Ferro", "Cap.")
    myGraph.addEdge("Homem Aranha", "Cap.")
    myGraph.addEdge("Homem Aranha", "Homem de Ferro")
    myGraph.addEdge("Pantera Negra", "Homem de Ferro")
    myGraph.addEdge("Pantera Negra", "Cap.")
    myGraph.addEdge("Pantera Negra", "Princess")
    myGraph.addEdge("Princess","Pantera Negra")
    myGraph.addEdge("Cap.","Pantera Negra")
    myGraph.addEdge("Homem de Ferro","Pantera Negra")
    myGraph.addEdge("Homem de Ferro", "Homem Aranha")
    myGraph.addEdge("Princess", "Homem de Ferro")
    myGraph.addEdge("Cap.", "Homem de Ferro")
    # myGraph.show()
    myGraph.showNodes()
    print('\n\n\n')

    result = myGraph.dijkstra("Little Abner")
    print("Dijkstra from Little Abner: ", result)
    result = myGraph.dijkstra("Cap.")
    print("Dijkstra from Cap.: ", result)
    result = myGraph.dijkstra("Homem de Ferro")
    print("Dijkstra from Homem de Ferro: ", result)
    result = myGraph.dijkstra("Homem Aranha")
    print("Dijkstra from Homem Aranha: ", result)
    result = myGraph.dijkstra("Pantera Negra")
    print("Dijkstra from Pantera Negra: ", result)
    result = myGraph.dijkstra("Princess")
    print("Dijkstra from Princess: ", result)