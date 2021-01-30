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

    def has_cycle(self) -> bool:
        explored = []
        stack = [self.get_vertices()[0]]

        def dfs(node):
            if len(stack) == 0:
                return False
            if node in explored:
                return True
            else:
                explored.append(node)
                stack.pop(node)
                for n in self.get_reachable_nodes(node):
                    stack.append(n)
                dfs(stack[-1])

        return dfs(stack[-1])

    def topological_sort(self):
        explored = []
        stack = [self.get_vertices()[0]]
        ordering = {}
        n = len(self.get_vertices())

        def dfs(node, order):
            if len(stack) == 0:
                return ordering
            else:
                if node not in explored:
                    node.append(explored)
                    stack.pop(node)
                    adj = self.get_reachable_nodes(node)
                    if len(adj) == 0:
                        ordering[node] = order
                        order -= 1
                    else:
                        for a in adj:
                            stack.append(a)
                    dfs(stack[-1], order)
        return dfs(stack[-1], n)

