"""
https://www.eolymp.com/en/submissions/13808348
"""


class Graph:

    def __init__(self, size):
        self.vertices = {
            v: set() for v in range(1, size + 1)
        }

    def add_edge(self, source, destination):
        self.vertices[source].add(destination)
        self.vertices[destination].add(source)

    def is_complete(self):
        n = len(self.vertices)
        for i in range(1, n + 1):
            if len(self.vertices[i]) != n - 1:
                return False
        return True


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for vertex in range(m):
            graph.add_edge(*map(int, f.readline().split()))

    if graph.is_complete():
        print("YES")
    else:
        print("NO")
