# Lowest common ancestor in binary tree

class Tnode():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        print "d:{} l:{} r:{}".format(self.data, self.left, self.right)

def max_depth(node):
    pass

def dfs(node):
    if node == None:
        return
    print node.data,
    dfs(node.left)
    dfs(node.right)

def build_tree(N):
    dlist = [x for x in range(1, N+1)]
    root = Tnode(dlist.pop(0))
    queue = []
    queue.append(root)
    while queue and dlist:
        node = queue.pop(0)
        node.left = Tnode(dlist.pop(0))
        queue.append(node.left)
        if dlist:
            node.right = Tnode(dlist.pop(0))
            queue.append(node.right)
    return root

def print_tree(node):
    queue = []
    sentinal  = Tnode(-1)

    queue.append(node)
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

def path_search(node, data):
    if node == None:
        return None
    if node.data == data:
        path = []
        path.insert(0, node.data)
        return path
    path = path_search(node.left, data)
    if path:
        path.insert(0, node.data)
        return path
    path = path_search(node.right, data)
    if path:
        path.insert(0, node.data)
        return path

def lcs(node, a, b):
    a_path = path_search(root, a)
    b_path = path_search(root, b)
    for i in range(min(len(a_path), len(b_path))):
        if a_path[i] != b_path[i]: return a_path[i-1]




root = build_tree(10)
#print_tree(root)
#dfs(root)
print lcs(root, 8, 5)

