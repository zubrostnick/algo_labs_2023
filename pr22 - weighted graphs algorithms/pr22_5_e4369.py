from collections import deque

"""
https://www.eolymp.com/uk/submissions/13814071
"""


class Graph:

    def __init__(self, size):
        self.vertices = {
            v: set() for v in range(1, size + 1)
        }

    def add_edge(self, u, v):
        self.vertices[u].add(v)
        self.vertices[v].add(u)

    def bfs(self, start_points):

        distances = {
            s: 10**5 for s in range(1, len(self.vertices) + 1)
        }

        for s in start_points:
            distances[s] = 0

        queue = deque(start_points)

        while queue:
            i = queue.popleft()

            for neighbour in self.vertices[i]:
                if distances[neighbour] > distances[i]:
                    distances[neighbour] = distances[i] + 1
                    queue.append(neighbour)

        return distances


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            graph.add_edge(*map(int, f.readline().split()))

        ans = 0

        k = int(f.readline())
        distances = graph.bfs(list(map(int, f.readline().split())))
        max_pair = max(distances.items(), key=lambda x: x[1])
        print(max_pair[-1], max_pair[0], sep='\n')



