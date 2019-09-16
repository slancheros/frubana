from tree import Tree


def generate_edge_tuple(str_tuple):
    list_pair = str_pair.split()
    print(list_pair)
    list_pair = [int(i) for i in list_pair]
    pair = tuple(list_pair)
    return pair


str_n = input("Enter number of nodes:")
n = int(str_n)
str_nodes = input("Enter colors for nodes:")
tree_node_list = str_nodes.split(' ')
tree_edges = list()
for node_color in range(0, n - 1):
    str_pair = input("Enter node pair: ")
    tuple_pair = generate_edge_tuple(str_pair)
    tree_edges.append(tuple_pair)

tree = Tree(n, tree_node_list, tree_edges)
tree.calculate_tree_sum()
tree.display_tree_sum()

