"""
Binary Search Tree implementation
"""

from lib.binarytree import BinaryTree, Node


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

    def inorder_successor(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, node, val):
        """
        Delete node from a bst
        - Leaf node: Just delete and return none
        - single child: Return child node to parent
        - Two children: Find inorder successor. Copy inorder successors data into
          node, and recursively delete inorder successor
        """

        if node is None:
            return None

        if node.data == val:
            if node.left is None and node.right is None:
                # leaf node
                return None
            elif node.left is None or node.right is None:
                # single child
                return node.right if not node.left else node.left
            else:
                # node with two children
                succ = self.inorder_successor(node.right)
                node.data = succ.data
                node.right = self.delete(node.right, succ.data)
        else:
            if val < node.data:
                node.left = self.delete(node.left, val)
            elif val > node.data:
                node.right = self.delete(node.right, val)


    def insert_node(self, node, val):
        if node is None:
            return Node(val)
        if val < node.data:
            node.left = self.insert_node(node.left, val)
        elif val > node.data:
            node.right = self.insert_node(node.right, val)

        return node

    def insert(self, val):
        """ Insert recursive into binary tree """
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_node(self.root, val)

    def delete(self, val):
        pass

if __name__ == '__main__':
    bst = Bst()
    input = [100, 20, 500, 10, 30, 40, 50, 400]
    for val in input:
        bst.insert(val)
    bst.print_levelorder()
    bst.print_inorder(bst.root)


