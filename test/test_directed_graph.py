from source.directed_graph import DirectedGraph


def test_has_cycle():
    cyclic_graph = DirectedGraph(vertices=[1, 2, 3], edges=[(1, 2), (2, 3), (3, 1)])
    assert(cyclic_graph.has_cycle(node=1, explored=[], stack=[1]))
    dag = DirectedGraph(vertices=[1, 2, 3], edges=[(1, 2), (2, 3)])
    assert(not dag.has_cycle(node=1, explored=[], stack=[1]))
