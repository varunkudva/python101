import unittest
from lib.binarytree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        items = [4, 8, 12, 11, 9, 13]
        for elem in items:
            self.tree.insert(elem)
    def test_insert(self):
        self.tree.print_levelorder()
        self.assertTrue(1)
        # lines = res.split()
        # self.assertEquals(lines[0], [4])
        # self.assertEquals(lines[1], [8, 12])
        # self.assertEquals(lines[2], [11, 9, 13])
    def test_path(self):
        res = self.tree.path_search(9)
        self.assertEquals(res, [4, 8, 9])
    def test_delete(self):
        pass
    def test_traversal(self):
        pass
    def test_dfs(self):
        pass
    def test_bfs(self):
        pass

if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBinaryTree)
    unittest.TextTestRunner(verbosity=2).run(suite)
