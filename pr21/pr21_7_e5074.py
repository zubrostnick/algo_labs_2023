"""
https://www.eolymp.com/uk/submissions/13808052
"""

class GraphNodeDegrees:

    def __init__(self, size):
        self.vertices = {
            v: 0 for v in range(1, size + 1)
        }

    def add_edge(self, source, destination):
        self.vertices[source] += 1
        self.vertices[destination] += 1

    def get_node_degree(self, key):
        return self.vertices[key]


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = GraphNodeDegrees(n)

        for vertex in range(m):
            graph.add_edge(*map(int, f.readline().split()))

    for i in range(1, n + 1):
        print(graph.get_node_degree(i))
