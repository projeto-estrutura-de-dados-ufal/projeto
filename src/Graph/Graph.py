import sys
class Graph:
    def __init__(self):
        self.nodes = 0
        self.edges = 0
        self.matrix = {}

    def showGraph(self):
        self.show()
        print('\n\n')
        self.showNodes()
        print('\n')
        print("Nodes: ", self.nodes)
        print("Edges: ", self.edges)
        print('\n\n\n')
        return ""
    
    def addNode(self, name):
        self.matrix[name] = dict.fromkeys(self.matrix.keys(), 0) 
        for lineIndex in self.matrix:
            self.matrix[lineIndex][name] = 0
        
        self.nodes += 1
    
    def removeNode(self, name):
        result = self.matrix.pop(name, None)

        if (result == None):
            return False

        for i in result:
            if (result[i] == 1):
                self.edges -= 1

        for line in list(self.matrix):
            for column in list(self.matrix[line]):
                if (column == name):
                    if (self.matrix[line][column] == 1):
                        self.edges -= 1
                    self.matrix[line].pop(column, None)

        self.nodes -= 1

        return True

    def addEdge(self, nodeName1, nodeName2):
        if (self.matrix[nodeName1][nodeName2] == 1):
            return False

        self.matrix[nodeName1][nodeName2] = 1
        self.edges += 1
        return True

    def removeEdge(self, nodeName1, nodeName2):
        if (self.matrix[nodeName1][nodeName2] == 0):
            return False

        self.matrix[nodeName1][nodeName2] = 0
        self.edges -= 1
        return True
    
    def search(self,id):
        if id in self.matrix :
            print(self.matrix[id])
            return self.matrix[id]
            
    def show(self):
        for line in self.matrix:
            print(line, self.matrix[line])
    
    def showNodes(self):
        for line in self.matrix:
            for column in self.matrix[line]:
                if (self.matrix[line][column] == 1):
                    print(line, "-->", column)

    def relax(self, distancesDict, predecessorsDict, u, v):
        weight = 1
        if (v):
            if (distancesDict[v] > distancesDict[u] + weight):
        # print(v, u, weight)
                distancesDict[v] = distancesDict[u] + weight
                predecessorsDict[v] = u

        return [distancesDict, predecessorsDict]

    def existsOpened(self, openedDict):
        for item in self.matrix:
            if (openedDict[item]):
                return True

        return False

    def lessDistance(self, openedDict, distancesDict):
        counter = 0
        lessItem = ""
        for item in self.matrix:
            counter += 1
            lessItem = item
            if (openedDict[item]):
                break
        
        if (counter > self.nodes):
            return -1
        
        nextItems = {}

        counter2 = 0
        for (key, value) in self.matrix.items():
            if (counter2 < counter):
                counter2 += 1
                continue 
            
            nextItems[key] = value
            counter2 += 1

        for i in nextItems:
            if (i == lessItem):
                continue

            if (openedDict[i] and distancesDict[lessItem] > distancesDict[i]):
                lessItem = i
        
        return lessItem


    def dijkstra(self, sourceId):
        distancesDict = {}
        predecessorsDict = {}
        openedDict = {}

        for item in self.matrix:
            distancesDict[item] = int(sys.maxsize / 2)
            predecessorsDict[item] = -1
            openedDict[item] = True

        distancesDict[sourceId] = 0

        while self.existsOpened(openedDict):
            u = self.lessDistance(openedDict, distancesDict)
            openedDict[u] = False

            if (u != -1):
                adjacency = dict()
                for (key, value) in self.matrix[u].items():
                    if (value == 1):
                        adjacency[key] = value

                # print(":",u)
                # print("---> ", adjacency)
                for i in adjacency:
                    # print(i)
                    relaxResult = self.relax(distancesDict, predecessorsDict, u, i)
                    distancesDict = relaxResult[0]
                    predecessorsDict = relaxResult[1]
                
                # print(distancesDict)
                # print(openedDict)
            
        return distancesDict
