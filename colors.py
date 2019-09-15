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
        path_list = self.find_path_bfs(i,j)
        color_list = list()
        for tuple_element in path_list:
            for id in tuple_element:
                color = self.nodes[id]
                if color not in color_list:
                    color_list.append(color)
        return len(color_list)

    # def find_path_bfs(self, i, j):
    #     path = list()
    #     if i == j:
    #         path.append((i,j))
    #     else:
    #         filtered_edges = filter(lambda x: self.contains_edge(i, x), self.edges)
    #         list_filtered_edges = list(filtered_edges)
    #         for current_edge in list_filtered_edges:
    #             if self.contains_edge(j, current_edge):
    #                 path.append(current_edge)
    #             elif not self.is_leaf(current_edge,i):
    #                 next_source = filter(lambda x: x != i, current_edge)
    #                 for item_next_source in next_source:
    #                     int_next_source = item_next_source
    #                     path.append(current_edge)
    #                     path.append(self.find_path_bfs(int_next_source, j))
    #     return path

    def find_path_bfs(self,i,j):
        path = list()
        visited = list()
        if i == j:
            path.append((i,j))
        else:
            filter_edges_with_i = filter(lambda x: self.contains_edge(i, x), self.edges)
            edges_to_visit= list(filter_edges_with_i)
            while len(edges_to_visit) > 0:
                for current_edge in edges_to_visit:
                    visited.append(current_edge)
                    if self.contains_edge(j,current_edge):
                        path.append(current_edge)
                        edges_to_visit.clear()
                    elif not self.is_leaf(current_edge,i):
                        path.append(current_edge)
                        next_source = filter(lambda x: x != i, current_edge)
                        for item_next_source in next_source:
                            filter_add_to_visit = filter(lambda x: self.contains_edge(item_next_source, x), self.edges)
                            add_to_visit = list(filter_add_to_visit)
                            add_to_visit_exclude_visited=[i for i in add_to_visit if i not in visited]
                            edges_to_visit += add_to_visit_exclude_visited
                    else:
                        edges_to_visit.remove(current_edge)
        return path

    def is_leaf(self, current_tuple, i):
        other_element_filter = filter(lambda x: x != i, current_tuple)
        for other_element in other_element_filter:
            int_other_element = other_element
        filtered_edges_by_other = filter(lambda x: self.contains_edge(int_other_element, x), self.edges)
        if len(list(filtered_edges_by_other)) == 1:
            return True
        else:
            return False

    @staticmethod
    def contains_edge(any_number, tuple_arg):
        if tuple_arg[0] == any_number or tuple_arg[1] == any_number:
            return True
        else:
            return False

    def calculate_sum_for_node(self, i):
        sum_colors_node = 0
        for index in range(1, n):
            sum_colors_node += self.calculate_amount_colors(i, index)

        self.colors_per_node_list.insert(i,sum_colors_node)
        return sum_colors_node

    def calculate_tree_sum(self):
        for i in range(0, n-1):
            self.calculate_sum_for_node(i+1)

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
print(tree.nodes)
print(tree.edges)
tree.calculate_tree_sum()
print (tree.display_tree_sum())
