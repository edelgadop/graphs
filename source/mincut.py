import os
from copy import deepcopy

from source.graph import Graph


def main():
    mincut = 9999
    current = 0
    graph_descr = read_graph(os.environ['GRAPH_PATH'])
    maxiter = 1000

    for n in range(maxiter):
        vertices = deepcopy(graph_descr["vertices"])
        edges = deepcopy(graph_descr["edges"])
        g = Graph(vertices=vertices, edges=edges)  # TODO Investigate why this constructor is passing-by-reference
        g.remove_duplicate_edges()
        gc = calculate_min_cut(g)
        current = len(gc.get_edges())
        if current < mincut:
            mincut = current
        print("Iteration " + str(n) + " of " + str(maxiter) + ". Current cut: " + str(current) + ", Min cut: " + str(mincut))


def read_graph(file: str):
    vx = []
    edx = []
    with open(file) as fd:
        lines = [line for line in fd.readlines()]
        for line in lines:
            vector = line.split("\t")
            node = int(vector[0])
            vx.append(node)
            for idx in range(1, len(vector) - 1):
                edx.append((node, int(vector[idx])))
    return {"vertices": vx, "edges": edx}


def calculate_min_cut(g: Graph) -> Graph:
    while len(g.get_vertices()) > 2:
        g.random_contraction()
    return g


if __name__ == "__main__":
    main()
