"""
Binary Tree
"""

class Node(object):
    ''' Node of a tree '''

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        print "d:{} l:{} r:{}".format(self.data, self.left, self.right)


class BinaryTree(object):
    """
    Binary Tree Class.
    Methods to insert, delete, traverse etc.
    """

    def __init__(self):
        """ Initialize root and other metadata """
        self.root = None

    def insert(self, val):
        ''' Insert Node into Binary Tree '''

        if self.root is None:
            new = Node(val)
            self.root = new
        else:
            queue = [self.root]  # level order queue
            while queue:
                node = queue.pop(0)
                if node.left == None:
                    node.left = Node(val)
                elif node.right == None:
                    node.right = Node(val)
                else:
                    queue.append([node.left, node.right])

    def delete(self, val):
        pass

    def max_depth(self, node):
        if node is None:
            return 0
        return max(self.max_depth(node.left), self.max_depth(node.right)) + 1

    def dfs(self, node, val):
        """ DFS to find a value in binary tree """

        if node is None:
            return None
        elif node.data == val:
            return node
        else:
            return self.dfs(node.left, val) or self.dfs(node.right, val)

    def print_inorder(self, node=None):
        if node is not None:
            self.print_inorder(node.left)
            print node.data,
            self.print_inorder(node.right)

    def print_preorder(self, node=None):
        if node is not None:
            print node.data,
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_levelorder(self):
        """
        Print tree in level order fashion.
        Sentinel element demarcates each level
        :return: None
        """
        if self.root is None: return

        queue = [self.root]
        sentinal = Node(-1)

        queue.append(sentinal)
        while queue:
            node = queue.pop(0)
            if node.data == -1:
                print
                if queue:
                    queue.append(sentinal)
            else:
                print node.data,
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

    def path_search(self, node, data):
        """ Print path to a node """
        if node == None:
            return None
        if node.data == data:
            path = []
            path.insert(0, node.data)
            return path
        path = self.path_search(node.left, data)
        if path:
            path.insert(0, node.data)
            return path
        path = self.path_search(node.right, data)
        if path:
            path.insert(0, node.data)
            return path
