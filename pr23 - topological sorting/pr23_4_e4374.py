"""
https://www.eolymp.com/uk/submissions/13816535
"""

import copy


class Graph:

    def __init__(self, size):
        self.vertices = {
            v: set() for v in range(1, size + 1)
        }
        self.edges = {}

    def add_edge(self, u, v):
        self.vertices[u].add(v)
        self.vertices[v].add(u)
        self.edges[len(self.edges) + 1] = (u, v)

    @staticmethod
    def dfs(vertices, start, visited):
        visited.add(start)
        # для всіх сусідів стартового елементу
        for neighbour in vertices[start]:
            if neighbour not in visited:  # які ще не були відвідані
                Graph.dfs(vertices, neighbour, visited)  # запускаємо DFS

    def execute_task(self, vert_delete):
        vert_new = copy.deepcopy(self.vertices.copy())

        for vert in vert_delete:
            print(vert, self.vertices)
            a, b = self.edges[vert]
            vert_new[a].remove(b)
            vert_new[b].remove(a)

        visited = set()  # відвідані вершини
        self.dfs(vert_new, 1, visited)

        for v in vert_new:
            if v not in visited:  # якась з вершин не була відвідана під час обходу
                print("Disconnected")   # то граф не є зв'язним
                return

        print("Connected")


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            graph.add_edge(*map(int, f.readline().split()))

        for i in range(int(f.readline())):
            n, *edges = map(int, f.readline().split())
            graph.execute_task(edges)

