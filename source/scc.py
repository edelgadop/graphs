import os

from source.directed_graph import DirectedGraph
from collections import defaultdict

t = 0  # Finishing time
s = 0  # Leader tag
f = [] # 2nd pass nodes
leaders = {}
explored = []


def reverse_graph(g: DirectedGraph) -> DirectedGraph:
    reversed_edges = [(j, i) for (i, j) in g.get_edges()]
    return DirectedGraph(g.get_vertices(), reversed_edges)


def dfs_loop(g: DirectedGraph, first: bool, paths: dict):
    global t
    global s
    global leaders
    global explored
    t = 0
    s = 0
    vertices = g.get_vertices()
    explored = []
    leaders = {}
    n = len(vertices)
    for i in reversed(range(n)):
        if first:
            v = vertices[i]
        else:
            v = f[i]
        if v not in explored:
            s = v
            dfs(g, v, paths)


def dfs(g: DirectedGraph, i: int, paths: dict):
    global t
    global f
    global leaders
    explored.append(i)
    leaders[i] = s
    if i in paths.keys():
        for j in paths[i]:
            print(j[1])
            if j[1] not in explored:
                dfs(g, j[1], paths)
    else:
        t = t + 1
        f.append(i)
        print("LOG: Finished node " + str(i))


def read_graph(file: str):
    vx = []
    edx = []
    paths = {}
    with open(file) as fd:
        lines = [line for line in fd.readlines()]
        node_prev = -1
        paths["direct"] = {}
        for line in lines:
            vector = line.split(" ")
            node = int(vector[0])
            if node != node_prev:  # input nodes are sorted
                vx.append(node)
                paths["direct"][node] = []
            for idx in range(1, len(vector) - 1):
                edx.append((node, int(vector[idx])))
                paths["direct"][node] += [(node, int(vector[idx]) )]
            node_prev = node
    return {"vertices": vx, "edges": edx, "paths": paths}


def compute_reverse_paths(edges: list, paths: dict):
    rev_edges = [tuple(reversed(e)) for e in edges]
    rev_edges = sorted(rev_edges, key=lambda x: x[0])
    paths["reverse"] = {}
    node_prev = -1
    for edge in rev_edges:
        node = edge[0]
        if node != node_prev:
            paths["reverse"][node] = []
        paths["reverse"][node] += [edge]
        node_prev = node
    return paths


def main():
    print("Reading graph ... ")
    source = read_graph(os.environ['GRAPH_PATH_SCCS'])

    print("Building graph ... ")
    graph = DirectedGraph(vertices=source["vertices"], edges=source["edges"])
    print("Starting Kosaraju Algorithm for SCC detection ... ")
    print("Computing reverse graph ...")
    graph_rev = reverse_graph(graph)
    print("Computing reverse paths ...")
    paths = compute_reverse_paths(source["edges"], source["paths"])
    print("Starting first DFS pass (reverse graph)")
    dfs_loop(graph_rev, first=True, paths=paths["reverse"])  # 1st pass: discover sink nodes of SCCs (leaders)
    print("First DFS pass completed.")

    print("Starting Second DFS pass (direct graph)")
    dfs_loop(graph, first=False, paths=paths["direct"])  # 2nd pass: explore SCCs
    print("Second DFS pass completed.")

    sccs = defaultdict(int)
    for k, v in leaders.items():
        sccs[v] += 1

    print("Top 5 components: ")
    top = 5
    sorted_sccs = {k: v for k, v in sorted(sccs.items(), key=lambda item: item[1])}
    n_sccs = len(sorted_sccs)
    if n_sccs < top:
        print(sorted_sccs)
    else:
        print(sorted_sccs[0:top-1])


if __name__ == "__main__":
    main()
