class Stack:
    def __init__(self):
        self.myList = []
        self.limit = 100
        self.size = 0
    
    def insert(self,item):
        if (self.size >= self.limit):
            return
        self.myList.append(item)
        self.size += 1
        

    def remove(self):
        if (self.size == 0):
            return False 
            
        self.myList.pop(self.size-1)        
        self.size -= 1
        return True

    def tam(self):
        print("O tamanho é:",self.size)

    def search(self,item):
        for i in range(self.size):
            if ("id",item) in self.myList[i].items():
                return i

        return -1
    
    def show(self):
        for i in range(self.size):
            print(self.myList[i])


