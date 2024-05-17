WHITE = 0 # Вершина білого кольору - вершина ще не відвідана
GRAY = 1 # Вершина сірого кольору - під час DFS ввійшли у вершину
BLACK = 2 # Вершина чорного кольору - під час DFS вийшли з вершини


class Graph:

    def __init__(self, size):
        self.vertices = {
            v: set() for v in range(1, size + 1)
        }

        self.colors = {
            v: 0 for v in range(1, size + 1)
        }

        self.stack = []
        self.over = False

    def add_edge(self, u, v):
        self.vertices[u].add(v)

    def topological_sorting(self):
        for vertex in self.vertices:
            if self.over:
                break
            self.dfs(vertex)

        sequence = []
        while self.stack:
            sequence.append(self.stack.pop())
        return sequence

    def dfs(self, vertex):
        if self.over:
            return

        if self.colors[vertex] == BLACK:
            return

        if self.colors[vertex] == GRAY:
            self.over = True
            self.stack = [-1]
            return

        self.colors[vertex] = GRAY
        for neighbour in self.vertices[vertex]:
            self.dfs(neighbour)

        self.colors[vertex] = BLACK
        self.stack.append(vertex)


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            graph.add_edge(*map(int, f.readline().split()))

    print(*graph.topological_sorting())







