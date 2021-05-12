class StaticList:
    def __init__(self):
        self.limit = 50
        self.myList = []
        self.size = 0

    def insert(self, node):
        if (self.size >= self.limit):
            return

        self.myList.append(node)
        self.size += 1