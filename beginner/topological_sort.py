# NOTE:
# OOP implementation of a graph!
# Use defaultdict with elements defaulted to list for edge list!
# The following algorithm applies too when first element of V has no incoming edge as will be pushed to end of sorted!


from collections import defaultdict


class Graph:

    def __init__(self, V):
        """
        Modify DFS to find Topological Sorting of a graph.

        https://www.geeksforgeeks.org/topological-sorting/

        """

        self.V = V  # vertex set as list
        self.E = defaultdict(list)  # edge set as dict

    def add_edge(self, u, v):

        self.E[u].append(v)

    def topological_sort_util(self, u, visited, sorted):

        visited[u] = True

        for v in self.E[u]:
            if not visited[v]:
                self.topological_sort_util(v, visited, sorted)

        sorted.insert(0, u)

    def topological_sort(self):

        visited = {}
        for v in self.V:
            visited[v] = False
        sorted = []

        for u in self.V:
            print(u)
            if not visited[u]:
                self.topological_sort_util(u, visited, sorted)

        return sorted


if __name__ == '__main__':
    g = Graph(list(range(6)))
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print(g.topological_sort())

    g = Graph(['a','b','c'])
    g.add_edge('b', 'c')
    g.add_edge('b', 'a')

    print(g.topological_sort())
