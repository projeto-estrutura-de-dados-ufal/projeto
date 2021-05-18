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

    def insert(self, data):
        if (self.data == 0):
            self.data = data
            return

        if data['id'] <= self.data['id']:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)
        self.ExecuteBalance()

    def PrintTree(self):
        print(self.data['id'], end='')
        print("(", end='')
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
        print(")",end='')
