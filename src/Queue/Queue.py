class Queue:
    
    def __init__(self):
        self.fila = []
        self.limit=100
        self.size = 0  
        
    def insert(self,value):
        if(self.size >= self.limit):
            return
        self.fila.append(value)
        self.size +=1        

    def remove(self):
        if (self.size == 0):
            return False

        del self.fila[0]
        self.size-=1
        return True

    def tam(self):
        print("O tamanho é:",self.size)

    def search(self,value):

        for i in range(self.size):

            if("id",value)in self.fila[i].value():

                return i
        return -1


        return -1

    def show(self):
        for i in range(self.size):
            print(self.fila[i])
