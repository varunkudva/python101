class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def is_leaf(node):
            return True if node.left == node.right == None else False

        def get_next_leaf(stack):
            while stack:
                node = stack.pop()
                if is_leaf(node):
                    return node

                if node.left:
                    stack1.append(node)
                    get_next_leaf(node.left)
                if node.right:
                    get_next_leaf(node.right)

        stack1 = [root1]
        stack2 = [root2]
        leaf1 = get_next_leaf(root1)
        leaf2 = get_next_leaf(root2)
        while leaf1 and leaf2:
            if leaf1.val != leaf2.val:
                return False
            leaf1 = get_next_leaf(root1)
            leaf2 = get_next_leaf(root2)
        return False
