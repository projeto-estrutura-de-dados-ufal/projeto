class StaticList:
    def __init__(self):
        self.limit = 10
        self.myList = []
        self.size = 0

    def insert(self,item):
        if (self.size >= self.limit):
            return
        self.myList.append(item)
        self.size += 1

    """
        item é um dicionário que possui uma chave 'id'
    """
    def insertOrdered(self, item):
        if (self.size >= self.limit):
            return False
        
        index = self.size

        while (index > 0 and self.myList[index - 1]['id'] > item['id']):
            index -= 1
        
        self.myList.insert(index, item)
        self.size += 1
        return True
    
    def show(self):
        for i in range(self.size):
            print(self.myList[i])
            print("\n")

    def tam(self):
        print("O tamanho é:",self.size)
    
    def search(self,item):
        for i in range(self.size):
            if ("id",item) in self.myList[i].items():        #print("Sim, está aqui") 
                return i

        return -1
        

    def binarySearch(self, id):
        left = 0
        right = self.size - 1

        while (left <= right):
            middle = round((left + right) / 2)

            if (self.myList[middle]["id"] == id):
                return middle
    
            
            if (self.myList[middle]["id"] < id):
                left = middle + 1
            else:
                right = middle - 1
        
        return -1 
    
    def remove(self, id):
        index = self.search(id)
        if (index == -1):
            return False 

        self.myList.pop(index)        

        self.size -= 1
        return True 
            
           


            
    
