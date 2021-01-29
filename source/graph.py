import random


class Graph:

    def __init__(self, vertices: list, edges: list):
        """
        Constructor
        :param vertices: list of vertices
        :param edges: list of edges
        """
        self.__vertices = vertices
        self.__edges = edges

    def print_ids(self):
        """
        :return:
        """
        print("Vertices: " + str(id(self.__vertices)))
        print("Edges: " + str(id(self.__edges)))

    def add_node(self, node):
        """
        Adds a node
        :param node: vertex to be added
        :return:
        """
        if node not in self.__vertices:
            self.__vertices.append(node)
        else:
            print("Duplicate node will not be appended")

    def remove_node(self, node):
        """
        Removes a node from the graph
        :param node: the vertex to be removed
        :return:
        """
        if node in self.__vertices:
            self.__vertices.remove(node)
        else:
            print("Can't remove node")

    def add_edge(self, edge: tuple):
        """
        Adds an edge to the graph
        :param edge:
        :return:
        """
        if (edge[0] in self.__vertices) and (edge[1] in self.__vertices) and (edge not in self.__edges):
            self.__edges.append(edge)
        else:
            print("Wrong edge definition: either impossible or duplicate")

    def remove_edge(self, edge: tuple):
        """
        Removes an edge from the graph
        :param edge:
        :return:
        """
        if edge in self.__edges:
            self.__edges.remove(edge)
        else:
            print("Can't remove edge")

    def get_vertices(self) -> list:
        """
        Accessor method for the vertices
        :return:
        """
        return self.__vertices

    def get_edges(self) -> list:
        """
        Accessor vertices for the edges
        :return:
        """
        return self.__edges

    def is_duplicated(self, edge: tuple) -> bool:
        """
        Tests whether an edge is duplicated or not within the graph
        :param edge:
        :return:
        """
        if ((edge[1], edge[0]) in self.__edges) or (edge in self.__edges):
            return True
        else:
            return False

    def get_duplicate_edges(self) -> list:
        """
        Finds and returns a list with the duplicated edges of the graph
        :return:
        """
        dupes = []
        for e in self.__edges:
            if (self.is_duplicated(e)) and ((e[1], e[0]) not in dupes):
                dupes.append(e)
        return dupes

    def get_edges_from_vertex(self, v) -> list:
        """
        Gets valid edges that can be traversed from vertex v
        :param v:
        :return:
        """
        if v not in self.__vertices:
            return []
        else:
            adj_edges = [e for e in self.__edges if e[0] == v]
            return adj_edges

    def get_reachable_nodes(self, v):
        """
        Returns a list of nodes which are reachable form V (adjacent nodes)
        :param v:
        :return:
        """
        if v in self.__vertices:
            adj_nodes = [n for n in self.__vertices if (v, n) in self.__edges]
            return adj_nodes
        else:
            print("Vertex not in graph")

    def remove_duplicate_edges(self):
        """
        Removes duplicate edges
        :return:
        """
        for e in self.get_duplicate_edges():
            self.__edges.remove(e)

    def random_contraction(self):
        """
        Implements the random contraction algorithm for an undirected graph
        Note: Caution. This method permanently modifies the graph. It is meant to be used as part
        of the mincut computation algorithm.
        :return:
        """
        # Select random edge
        current_edges = self.get_edges()
        random_edge = current_edges[random.randint(0, len(current_edges) - 1)]

        # Remove edge and vertices
        self.remove_edge(random_edge)
        self.__vertices.remove(random_edge[0])
        self.__vertices.remove(random_edge[1])

        # Create and add super node
        super_node = str(random_edge[0]) + "-" + str(random_edge[1])
        self.add_node(super_node)

        # Contract remaining edges
        contracted_edges = []
        for i in range(len(self.__edges)):
            if (str(self.__edges[i][0]) == str(random_edge[0])) or (str(self.__edges[i][0]) == str(random_edge[1])):
                contracted_edges.append((super_node, self.__edges[i][1]))
            elif (str(self.__edges[i][1]) == str(random_edge[0])) or (str(self.__edges[i][1]) == str(random_edge[1])):
                contracted_edges.append((self.__edges[i][0], super_node))
            else:
                contracted_edges.append(self.__edges[i])
        cleansed_edges = []
        for j in range(len(contracted_edges)):
            if (contracted_edges[j][0] in self.__vertices) and (contracted_edges[j][1] in self.__vertices):
                cleansed_edges.append(contracted_edges[j])
        self.__edges = cleansed_edges

    def find_min_distance(self, a, b) -> int:
        """
        Determines the distance form node A to node B with a Breadth-First-Search (BFS) approach
        :param a: first node
        :param b: second node
        :return: min distance
        """
        if (a not in self.__vertices) or (b not in self.__vertices):
            return -1
        elif a == b:
            return 0
        else:
            explored = {a: 0}
            queue = [a]
            while len(queue) != 0:
                v = queue.pop(0)
                for edge in self.get_edges_from_vertex(v):
                    w = edge[1]
                    if w == b:
                        return explored[v] + 1
                    elif w not in explored.keys():
                        explored[w] = explored[v] + 1
                        queue.append(w)
                    else:
                        pass  # Do nothing if previously seen
