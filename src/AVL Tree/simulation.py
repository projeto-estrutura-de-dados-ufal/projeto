class Node:
    def __init__(self, data):
        self.data = data
        self.next(None, None)
    
    def next(self, left, right):
        self.left = left
        self.right = right

    def balance(self):
        dep_left = 0
        if self.left:
            dep_left = self.left.depth()
        dep_right = 0
        if self.right:
            dep_right = self.right.depth()
        return dep_left - dep_right

    def depth(self):
        dep_left = 0
        if self.left:
            dep_left = self.left.depth()
        dep_right = 0
        if self.right:
            dep_right = self.right.depth()
        return 1 + max(dep_left, dep_right)

    def RotationLeft(self):
        self.data, self.right.data = self.right.data, self.data
        old_left = self.left
        self.next(self.right, self.right.right)
        self.left.next(old_left, self.left.left)

    def RotationRight(self):
        self.data, self.left.data = self.left.data, self.data
        old_right = self.right
        self.next(self.left.left, self.left)
        self.right.next(self.right.right, old_right)

    def RotationLeftRight(self):
        self.left.RotationLeft()
        self.RotationRight()

    def RotationRightLeft(self):
        self.right.RotationRight()
        self.RotationLeft()

    def ExecuteBalance(self):
        bal = self.balance()
        if bal > 1:
            if self.left.balance() > 0:
                self.RotationRight()
            else:
                self.RotationLeftright()
        elif bal < -1:
            if self.right.balance() < 0:
                self.RotationLeft()
            else:
                self.RotationRightLeft()

    def insere(self, data):
        if data <= self.data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insere(data)
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insere(data)
        self.ExecuteBalance()

    def PrintTree(self):
        # print( " " * indent + str(self.data))
        #     self.left.PrintTree(indent + 2)
        #     self.right.PrintTree(indent + 2)
        
        print(self.data, end='')
        print("(", end='')
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
        print(")",end='')
avltree = Node(7)
avltree.insere(1)
avltree.insere(9)
avltree.insere(5)
avltree.insere(10)
avltree.insere(12)
avltree.insere(14)
""
"TA FUNCIONANDO, ELE BALANCEOU"
"""ANTES                            DEPOIS
           7                                   7
        1     9                            1      10
          5     10                           5   9   12
                  12                                    14
                    14

"""
avltree.PrintTree()
print('\n')

