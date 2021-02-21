
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
    def __repr__(self):
        return "{} left: {} right {}".format(self.data, self.left, self.right)

class Bst:
    def __init__(self):
        self.root = None
        self.res = []

    def insert(self, data):
        if self.root:
            self.__insert(self.root, data)
        else:
            self.root = Node(data)

    def __insert(self, node, data):
        if node is None:
            new = Node(data)
            if self.root is None:
                self.root = new
            return new
        else:
           if data < node.data:
               node.left = self.__insert(node.left, data)
           elif data > node.data:
               node.right = self.__insert(node.right, data)
           return node

    def insert_iterative(self, node, data):
        if self.root is None:
            self.root = Node(data)
        else:
            node = self.root
            while node:
                if data < node.data:
                    if node.left is None:
                        node.left = Node(data)
                    else:
                        node = node.left
                elif data > node.data:
                    if node.right is None:
                        node.right = Node(data)
                    else:
                        node = node.right

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.res.append(node.data)
        self.inorder(node.right)
        return self.res

if __name__ == '__main__':
    arr = [1, 10, 2, 2, 10, 3, 3, 3, 4, 5, 5]
    bst = Bst()
    for item in arr:
        bst.insert(item)
    print(bst.inorder(bst.root))
