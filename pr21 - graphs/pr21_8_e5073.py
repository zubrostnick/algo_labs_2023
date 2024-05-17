"""
https://www.eolymp.com/uk/submissions/13808208
"""


class Graph:

    def __init__(self, size):
        self.vertices = {
            v: [] for v in range(1, size + 1)
        }

    def add_edge(self, source, destination):
        self.vertices[source].append(destination)

    def is_second_vertice(self, source, destination):
        return destination in self.vertices.get(source)


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)

        res = False
        for vertex in range(m):
            start, end = map(int, f.readline().split())

            if graph.is_second_vertice(start, end):
                res = True
                break
            graph.add_edge(start, end)

    if res:
        print("YES")
    else:
        print("NO")

