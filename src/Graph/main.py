from Graph import Graph
import pandas as pd
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from helpers import readData

if __name__ == "__main__":
    heroCsv = pd.read_csv('../../data/hero-network.csv')

    hero1 = heroCsv["hero1"]
    hero2 = heroCsv["hero2"]


    size = 8 
    heroes = []
    for i in range(size):
        # print(hero1[i], " --> ", hero2[i])
        if (hero1[i] not in heroes):
            heroes.append(hero1[i])

    for j in range(size):
        if (hero2[j] not in heroes):
            heroes.append(hero2[j])

    myGraph = Graph()

    for hero in heroes:
        myGraph.addNode(hero)
    
    for hero in range(size):
        # print(hero1[hero], hero2[hero])
        myGraph.addEdge(hero1[hero], hero2[hero])

    myGraph.showGraph()
    myGraph.removeNode(heroes[len(heroes) - 1])
    myGraph.showGraph()