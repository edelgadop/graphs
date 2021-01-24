from source.graph import Graph


def test_min_distance():
    vertices = [1, 2, 3, 4, 5, 6]
    edges = [(1, 2), (1, 3), (2, 4), (2, 3), (3, 4), (3, 5), (4, 5), (5, 6)]
    g = Graph(vertices=vertices, edges=edges)
    assert g.find_min_distance(1, 6) == 3
