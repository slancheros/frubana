def generate_edge_tuple(str_tuple):
    list_pair = str_pair.split()
    print(list_pair)
    list_pair = [int(i) for i in list_pair]
    pair = tuple(list_pair)
    return pair


class Tree:
    colors_per_node_list = list()

    def __init__(self, n, nodes, edges):
        self.n = n
        self.nodes = nodes
        self.edges = edges

    def calculate_amount_colors(self, i, j):
        path_list = self.has_path_bfs(i,j)
        color_list = list()
        for tuple_element in path_list:
            for color in tuple_element:
                if color not in color_list:
                    color_list.append(color)
        return len(color_list)

    def has_path_bfs(self, i, j):
        path = list()
        filtered_edges = filter(lambda x: self.contains_edge(i, x), self.edges)
        for current_edge in filtered_edges:
            if self.contains_edge(j, current_edge):
                path.append(current_edge)
            elif not self.is_leaf(current_edge,i):
                next_source = filter(self.filter_out_tuple(i,current_edge),current_edge)
                path.append ( self.has_path_bfs(next_source,j))
        return path

    def is_leaf(self, current_tuple, i):
        other_element_in_tuple = filter(lambda x: x != i, current_tuple)
        filtered_edges_by_other = filter(lambda x: self.contains_edge(other_element_in_tuple, x), self.edges)
        if filtered_edges_by_other == 1:
            return True
        else:
            return False

    def filter_function(self,any_number):
        if any([item for item in self.edges if item[0] == any_number or item[1] == any_number]):
            return True
        else:
            return False

    @staticmethod
    def contains_edge(any_number, tuple_arg):
        return tuple_arg[0] == any_number or tuple_arg[1] == any_number

    @staticmethod
    def filter_out_tuple(any_number,tuple_arg):
        if any(item for item in tuple_arg if item != any_number):
            return True
        else:
            return False

    def calculate_sum_for_node(self, i):
        sum_colors_node = 0
        for index in range(1, n-1):
            sum_colors_node += self.calculate_amount_colors(i, index)

        self.colors_per_node_list.insert(i,sum_colors_node)
        return sum_colors_node

    def calculate_tree_sum(self):
        for i in range(1, len(self.nodes)-1):
            self.calculate_sum_for_node(i)

    def display_tree_sum(self):
        for item in self.colors_per_node_list:
            print( item )


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
print(tree)
print(tree.nodes)
print(tree.edges)
tree.calculate_tree_sum()
print (tree.display_tree_sum())
