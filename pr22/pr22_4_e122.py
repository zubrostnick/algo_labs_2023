"""
https://www.eolymp.com/uk/submissions/13813919
"""


class Graph:

    def __init__(self, size):
        self.vertices = {
            v: set() for v in range(1, size + 1)
        }

    def add_edge(self, u, v):
        self.vertices[u].add(v)

    def dfs(self, start, finish, limit, visited):
        global ans
        if start == finish and len(visited) <= limit:
            ans += 1
            return
        if len(visited) > limit:
            return

        visited.add(start)
        # для всіх сусідів стартового елементу
        for neighbour in self.vertices[start]:
            if neighbour not in visited:  # які ще не були відвідані
                self.dfs(neighbour, finish, limit, visited.copy())  # запускаємо DFS


if __name__ == "__main__":
    with open("input.txt") as f:
        n, k, a, b, d = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(k):
            graph.add_edge(*map(int, f.readline().split()))

        ans = 0
        graph.dfs(a, b, d, set())
        print(ans)
