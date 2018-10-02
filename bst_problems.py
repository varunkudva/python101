from lib.bst import Bst

if __name__ == '__main__':
    bst = Bst()
    input = [9, 20, 11, 13, 5, 12]
    for val in input:
        bst.insert(val)

    bst.print_levelorder()
    #bst.print_inorder(bst.root)