from lib.binarytree import Node


def inorder(node):
    if node is None:
        return None
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def inorder_iterative(root):
    """
    """
    stack = []
    node = root
    while node or stack:
        # recursive inorder(root.left)
        while node:
            # keep going left until no more nodes left
            stack.append(node)
            node = node.left

        # no more nodes on left. print the current node
        # repeat for right subtree
        if stack:
            node = stack.pop()
        print(node.data)

        # recursive(node.right)
        node = node.right



def preorder(node:Node):
    if node is None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)

"""
with stacks, either you pass the arguments for next call in the stack or
preserve the state of current call in the stack. In preorder, since it
is tail recursion, there is nothing of current state to store in stack.
Just pass parameters in stack
"""
def preorder_iterative(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data)
        stack.append(node.right)
        stack.append(node.left)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node)

def postorder_it(root):
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack[-1]
        # process right
        if node.right:
            node = node.right

        # process node
        node = stack.pop()
        print(node)

    pass

"""
This is the validate bst problem. Check if the prev node in inorder traversal is
less than the current node
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        node = root
        prev, cur = None, None
        while node or stack:
            while node:
                # go leftmost till no nodes left
                stack.append(node)
                node = node.left
            # pop element from stack to find next node
            node = stack.pop()
            if prev:
                if node.val <= prev.val:
                    return False
            prev = node
            # go leftmost again with current node
            node = node.right
        return True
