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
    # myGraph.show()
    # print('\n')
    myGraph.addNode("Cap.")
    myGraph.addEdge("Homem de Ferro", "Cap.")
    myGraph.addEdge("Cap.", "Homem de Ferro")
    myGraph.show()
    print("\n")
    myGraph.showNodes()
    print("\n")
    print("Nodes: ", myGraph.nodes)
    print("Edges: ", myGraph.edges)

    print("\n\n")
    myGraph.removeNode("Cap.")
    myGraph.show()
    print("\n")
    myGraph.showNodes()
    print("\n")
    print("Nodes: ", myGraph.nodes)
    print("Edges: ", myGraph.edges)

    print('\n\n')
    myGraph.removeEdge("Little Abner", "Princess")
    myGraph.show()
    print("\n")
    myGraph.showNodes()
    print("\n")
    print("Nodes: ", myGraph.nodes)
    print("Edges: ", myGraph.edges)
