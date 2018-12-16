# coding=utf-8

def check_bst(node):
    lmax = -float('inf')
    rmax = float('inf')

    def is_bst(node, lmax, rmax):
        if lmax < node.data < rmax:
            return True, node.data
    is_bst(node.left, lmax, node.data)
    is_bst(node.right, node.data, rmax)
    if