class Node:
    """
        content é a linha do .csv transformada em dicionário
    """
    def __init__(self, content, next):
        self.content = content
        self.next = next


class LinkedList:
    def __init__(self):
        self.begin = None
        self.size = 0

    def getSize(self):
        return self.size

    def insert(self, item):
        """
        [None] => [item]
        [1] => [1, item]
        """
        if (self.begin == None):
            self.begin = Node(item, None)
            return True

        element = self.begin

        while (element.next != None):
            element = element.next

        element.next = Node(item, None)
        return True

            
    def show(self):
        element = self.begin
        while(element != None):
            print(element.content)
            element = element.next

    def search(self, id):
        currentElement = self.begin

        while (currentElement != None):
            if (currentElement.content['id'] == id):
                return currentElement
            
            currentElement = currentElement.next
        
        return None

    def searchForDelete(self, id):
        currentElement = self.begin
        previous = None

        while (currentElement != None and currentElement.content['id'] < id):
            previous = currentElement
            currentElement = currentElement.next
        
        if (currentElement != None and currentElement.content['id'] == id):
            return [previous, currentElement] 

        return None

    def delete(self, id):
        result = self.searchForDelete(id)

        if (result == None):
            return False

        previous = result[0]
        element = result[1]

        if (previous == None):
            self.begin = element.next
        else:
            previous.next = element.next

        return True

    def reboot(self):
        self.begin = None