"""
Binary Search Tree implementation
"""

from binarytree import BinaryTree, Node


class Bst(BinaryTree):
    def __init__(self):
        super(Bst, self).__init__()

    def insert_iterative(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            node = self.root
            while node is not None:
                if val < node.data:
                    if node.left is None:
                        node.left = Node(val)
                    node = node.left
                elif val > node:
                    if node.right is None:
                        node.right = Node(val)
                    node = node.right

    def insert(self, node, val):
        """ Insert recursive into binary tree """
        if self.root is None:
            self.root = Node(val)
        else:
            if node is None:
                return Node(val)
            if val < node.data:
                node.left = self.insert(node.left, val)
            elif val > node.data:
                node.right = self.insert(node.right, val)

            return node


        def delete(self, val):
            pass

if __name__ == '__main__':
    bst = Bst()
    input = [100, 20, 500, 10, 30, 40, 50, 400]
    for val in input:
        bst.insert(bst.root, val)
    bst.print_levelorder()
    bst.print_inorder(bst.root)


