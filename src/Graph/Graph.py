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
    
    def show(self):
        for line in self.matrix:
            print(line, self.matrix[line])
    
    def showNodes(self):
        for line in self.matrix:
            for column in self.matrix[line]:
                if (self.matrix[line][column] == 1):
                    print(line, "-->", column)