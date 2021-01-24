import random


class Graph:

    def __init__(self, vertices: list, edges: list):
        self._vertices = vertices
        self._edges = edges

    def get_ids(self):
        print("Vertices: " + str(id(self._vertices)))
        print("Edges: " + str(id(self._edges)))

    def add_node(self, node):
        if node not in self._vertices:
            self._vertices.append(node)
        else:
            print("Duplicate node will not be appended")

    def remove_node(self, node):
        if node in self._vertices:
            self._vertices.remove(node)
        else:
            print("Can't remove node")

    def add_edge(self, edge: tuple):
        if (edge[0] in self._vertices) and (edge[1] in self._vertices) and (edge not in self._edges):
            self._edges.append(edge)
        else:
            print("Wrong edge definition: either impossible or duplicate")

    def remove_edge(self, edge: tuple):
        if edge in self._edges:
            self._edges.remove(edge)
        else:
            print("Can't remove edge")

    def get_vertices(self) -> list:
        return self._vertices

    def get_edges(self) -> list:
        return self._edges

    def is_duplicated(self, edge: tuple) -> bool:
        if (edge[1], edge[0]) in self._edges:
            return True
        else:
            return False

    def get_duplicate_edges(self) -> list:
        dupes = []
        for e in self._edges:
            if (self.is_duplicated(e)) and ((e[1], e[0]) not in dupes):
                dupes.append(e)
        return dupes

    def remove_duplicate_edges(self):
        for e in self.get_duplicate_edges():
            self._edges.remove(e)

    def random_contraction(self):
        # Select random edge
        current_edges = self.get_edges()
        random_edge = current_edges[random.randint(0, len(current_edges) - 1)]

        # Remove edge and vertices
        self.remove_edge(random_edge)
        self._vertices.remove(random_edge[0])
        self._vertices.remove(random_edge[1])

        # Create and add super node
        super_node = str(random_edge[0]) + "-" + str(random_edge[1])
        self.add_node(super_node)

        # Contract remaining edges
        contracted_edges = []
        for i in range(len(self._edges)):
            if (str(self._edges[i][0]) == str(random_edge[0])) or (str(self._edges[i][0]) == str(random_edge[1])):
                contracted_edges.append((super_node, self._edges[i][1]))
            elif (str(self._edges[i][1]) == str(random_edge[0])) or (str(self._edges[i][1]) == str(random_edge[1])):
                contracted_edges.append((self._edges[i][0], super_node))
            else:
                contracted_edges.append(self._edges[i])
        cleansed_edges = []
        for j in range(len(contracted_edges)):
            if (contracted_edges[j][0] in self._vertices) and (contracted_edges[j][1] in self._vertices):
                cleansed_edges.append(contracted_edges[j])
        self._edges = cleansed_edges






