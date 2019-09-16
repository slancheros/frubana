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
                color = self.nodes[(id-1)]
                if color not in color_list:
                    color_list.append(color)
        return len(color_list)

    def find_path_bfs(self,i,j):
        path = list()
        visited = list()
        if i == j:
            path.append((i,j))
        else:
            filter_edges_with_i = filter(lambda x: self.contains_edge(i, x), self.edges)
            edges_to_visit= list(filter_edges_with_i)
            while len(edges_to_visit) > 0:
                if(i,j) in edges_to_visit or (j,i) in edges_to_visit:
                    path.clear()
                    if(i, j) in edges_to_visit:
                        path.append((i,j))
                    if(j, i) in edges_to_visit:
                        path.append((j, i))
                    edges_to_visit.clear()
                else:
                    for current_edge in edges_to_visit:
                        visited.append(current_edge)
                        if self.contains_edge(j,current_edge):
                            path.append(current_edge)
                            edges_to_visit.clear()
                        elif not self.is_leaf(current_edge,i):
                            if current_edge not in path:
                                path.append(current_edge)
                            next_source = filter(lambda x: x != i, current_edge)
                            for item_next_source in next_source:
                                filter_add_to_visit = filter(lambda x: self.contains_edge(item_next_source, x), self.edges)
                                add_to_visit = list(filter_add_to_visit)
                                add_to_visit_exclude_visited=[i for i in add_to_visit if i not in visited]
                                edges_to_visit += add_to_visit_exclude_visited
                        else:
                            edges_to_visit.remove(current_edge)

        self.remove_leaves_in_path(path,i,j)
        return path

    def remove_leaves_in_path(self, path, i, j):
        for tuple_item in path:
            other_element_filter = filter(lambda x: x != i and x != j, tuple_item)
            for other_element in other_element_filter:
                amount_elements_path = filter(lambda x: self.contains_edge(other_element, x), path)
                list_amount_elements_path = list(amount_elements_path)
                if len(list_amount_elements_path) == 1:
                    path.remove(list_amount_elements_path[0])

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
        for index in range(0, self.n):
            calculated = self.calculate_amount_colors(i, index+1)
            sum_colors_node += calculated
        self.colors_per_node_list.insert(index, sum_colors_node)
        return sum_colors_node

    def calculate_tree_sum(self):
        self.colors_per_node_list.clear()
        for i in range(0, self.n ):
            self.calculate_sum_for_node(i+1)

    def display_tree_sum(self):
        for item in self.colors_per_node_list:
            print( item )
        self.colors_per_node_list.clear()