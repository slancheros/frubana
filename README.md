# 1. Calculate List Median

## Files

The implementation made in the Python files:
1. median.py has the logic implementation of the list operations.
2. test_calculate_median.py contains unit tests for median values.
3. median_ui.py contains the user interaction logic for the solution.

## Logic implementation

Logic has been implemented by:
1. Calculating the median just when a value is added to the list
2. Divided in 4 cases:
   * When the list is empty (Basic)
   * When the list has one element (Basic)
   * When length is even
   * When length is odd
   
3. The method calculate_median in median.py is the core method. Other functions and methods have been created for support and to keep code
as clean as possible: short methods and code readable.

4. Some input validation is provided, and prompts for input  have been added. The output is as specified on the requirement.

5. It took approx. **2 hours and a half** to complete in effective time.

# 2. Unrooted Tree Color Sum


## Analysis

Firstly, by the definition of Unrooted Tree as:

>"An undirected graph with no cycles"<br>
> *-Thanks, Wikipedia*

I took some assumptions:
1. The tree will have no cycles. Since this is an assumption, there is no validation on the relations provided by the user, verifying that there are indeed no cycles.
2. The relations between nodes have no direction, meaning that a node can be found in first or last position (i,j) or (j,i), therefore the search for a path in the tree could start either way.
3. A node may have several relations, but this does not make it the root. 
4. A node in the tree is a leaf if only has one relation to another node.
5. A node can have many children, not only 2.
6. **There is always a path between 2 given nodes**

![Unrooted Tree Example](/images/unrooted tree.jpg "Simple Unrooted Tree")

This analysis took me to the following implementation:

## Implementation
### Files 
1. tree.py contains the class representing the Tree with its calculation methods.
2. colors.py has the user interaction logic.
3. test_tree.py unit tests for the Tree class.

I used the simplest implementation possible:

### Tree Class
It is composed of the 3 input elements provided in interaction with the user:
1. colors list. The index on this list is the node id for the tree nodes.
2. A list of edges,as provided by the user, representing the relations between nodes and implemented as Python tuples. The tuples contain the node id (index on color list), not the actual color or node. A node on the tree is the combination of this id, and the actual color (number) on the color list for that id.
3. The amount of nodes = n.

Python tuples were selected to store pairs, because a dictionary required the key to be unique, and as seen, the relations required 1 or more elements with the same "key".

### Logic Implementation for Node Sum

For obtaining the sum of all nodes:

1. A global list (colors_per_node_list) will store the sum for every node. The index on the list is the id of the node for which the calculation is performed.
2. The method that performs the sum of all nodes is calculate_tree_sum, which invokes the method calculate_sum_for_node(i), where i is the id of every node on the tree.
3.The calculate_sum_for_node_method, invokes all the possible different combinations of paths(i,x) where x goes from 1 to n in the tree for node i, and sums the amount of colors for each path to give a total for the node. For calculating the amount of colors in a path, this method invokes the calculate_amount_colors(i,j), where (i,j) is the path to be calculated.
4. The calculate_amount_colors_method(i,j) just count the colors in the path between 2 nodes. The path is the minimal list of edges taken to go from one node to the other. The path is calculated by the find_path_bfs(i,j), which is the interesting method on the implementation, since it is the one that performs the search of node destination(j), from a given node source(i) on the tree.

### Implementation of  the Find Path BFS method.

Since we are searching in an unrooted tree,  this is equivalent on searching on an undirected graph, then the strategy used is Breadth First Search. However, 

> No recursion was used for this implementation

The reason is that recursion easily got to its maximum level when used. Then an iterative solution was implemented with the following cases:

1. The path (i,i) is trivial case and returned a path with just one element = [(i,i)] (Basic)
2. If the path to look for was not the trivial case, the edges list of the tree were filtered by those containing i. This is the list of 
nodes to visit to start.
3. From there, the basic case is that one of the nodes is the pair (i,j), in which case, the path is only that element, then the search is over, and there are no more nodes to visit.
4. If (i,j) does not exist, then there should be a path to j that consist on a set of edges. To find it, we have to iterate on the list of nodes to visit, if one of them contains j.  Then is when the concept of leaf appears:
    * If the node is a leaf, meaning that it does not have any children, looking from the adjacent element of the tuple, and it does not contain j, it is not worth looking and its removed from the list of edges_to_visit.
    * If the node is **not** a leaf, then the node is added to the path, because it may contain the path to j. Then we iterate by adding the current node's children to the edges_to_visit list and removing from edges_to_visit the nodes already visited ( that we keep in another list).
    
5. At the end of this iteration we have a list of edges in the path list. However there are some edges that we have added that did not make part of the path from i to j, because in our last step( iteration) we added those edges with children and we didn't have a way to know if they indeed lead to j.

For that we use the remove_leaves_in_path(path, i, j). What this method does is to verify that every element on the path list has a link towards j. If there is an element that does not have that link, it means is a *leaf* to this list and should be removed. In this case, this a different *leaf* concept than that used in the tree search.

# Install requirements

* The code was implemented using Python 3.7 as interpreter and virtual env.
* Unit tests were developed with unittestcase module.

Anyway, hope you enjoy my implementation! Thank you!











