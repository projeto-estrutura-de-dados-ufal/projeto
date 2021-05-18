class Node:
    def __init__(self, content, id):
        self.content = content 
        self.id = id

class Graph:
    def __init__(self, maxSize):
        self.nodes = 0
        self.edges = 0
        self.matrix = []
        self.nextNode = 0
        self.nodesList = []
        self.maxSize = maxSize 

        for i in range(maxSize):
            self.matrix.append([0 for i in range(maxSize)])

    def add_edge(self, v1, v2):
        self.matrix[v1][v2] = 1
        return True
    
    def remove_edge(self, v1, v2):
        if (self.matrix[v1][v2] == 0):
            return False 
        self.matrix[v1][v2] = 0
        return True

    def add_node(self, content):
        newNode = Node(content, self.nextNode)
        self.nodesList.append(newNode)
        self.nextNode += 1
        self.nodes += 1

    def get_index(self, content):
        aList = list(filter(lambda item: (item.content == content), self.nodesList))

        if (len(aList) == 0):
            return -1 

        return self.nodesList.index(aList[0])

    def print_nodes(self):
        for i in self.nodesList:
            print(i.content, self.nodesList.index(i))

    def print_graph(self):
        for i in range(self.maxSize):
            for j in range(self.maxSize):
                if (self.matrix[i][j] == 1):
                    print(self.nodesList[i].content, "-->", self.nodesList[j].content)



