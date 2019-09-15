from unittest import TestCase
from colors import Tree


class TestTree(TestCase):

    myTree = None

    def setUp(self) -> None:
        self.myTree = Tree(5, [1, 2, 3, 2, 3], [(1, 2), (2, 3), (2, 4), (1, 5)])

    def test_calculate_amount_colors(self):
        count_colors = self.myTree.calculate_amount_colors(1,2)
        self.assertEquals(count_colors, 2)

    def test_find_path_bfs(self):
        path_to_test = self.myTree.find_path_bfs(1,4)
        self.assertEquals(path_to_test, [(1, 2), (2, 4)])

    def test_is_leaf(self):
        is_leaf = self.myTree.is_leaf((2,4),2)
        self.assertTrue(is_leaf)

    def test_is_not_leaf(self):
        is_leaf= self.myTree.is_leaf((1,2),1)
        self.assertFalse(is_leaf)

    def test_contains_edge(self):
        contains_number = Tree.contains_edge(1,(1,2))
        self.assertTrue(contains_number)

    def test_does_not_contain_edge(self):
        contains_number = Tree.contains_edge(4, (2, 3))
        self.assertFalse(contains_number)

    def test_calculate_sum_for_node_simple(self):
        sum_for_node = self.myTree.calculate_sum_for_node(1)
        self.assertEquals(sum_for_node, 10)

    def test_calculate_tree_sum(self):
        self.myTree.calculate_tree_sum()
        self.assertEquals(self.myTree.colors_per_node_list, [10,9,11,9,12])



