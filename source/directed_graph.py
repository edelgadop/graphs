from source.graph import Graph


class DirectedGraph(Graph):

    def is_duplicated(self, edge: tuple) -> bool:
        """
        Overrides super class method
        :param edge:
        :return:
        """
        if edge in self.get_edges():
            return True
        else:
            return False

    def has_cycle(self, node, explored: list, stack: list) -> bool:
        stack.pop(-1)
        if node in explored:
            return True
        else:
            explored.append(node)
            for n in self.get_reachable_nodes(node):
                stack.append(n)
            if len(stack) == 0:
                return False
            return self.has_cycle(stack[-1], explored, stack)

    def topological_sort(self):
        explored = []
        stack = [self.get_vertices()[0]]
        ordering = {}
        n = len(self.get_vertices())

        def dfs(node, order):
            if len(stack) == 0:
                return ordering
            else:
                stack.pop(node)
                if node not in explored:
                    node.append(explored)
                    adj = self.get_reachable_nodes(node)
                    if len(adj) == 0:
                        ordering[node] = order
                        order -= 1
                    else:
                        for a in adj:
                            stack.append(a)
                    dfs(stack[-1], order)

        return dfs(stack[-1], n)
