"""
https://www.eolymp.com/uk/submissions/13807960
"""

class Graph:

    def __init__(self, size):
        self.vertices = {
            v: [] for v in range(1, size + 1)
        }

    def add_edge(self, source, destination):
        self.vertices[source].append(destination)

    def adjacency_matrix(self):
        size = len(self.vertices)
        matrix = [
            [0 for j in range(size)] for i in range(size)
        ]
        for vertex in self.vertices:
            for neighbour in self.vertices[vertex]:
                i = vertex - 1
                j = neighbour - 1
                matrix[i][j] = 1
        return matrix


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for vertex in range(1, m + 1):
            graph.add_edge(*map(int, f.readline().split()))

    matrix = graph.adjacency_matrix()

    for i in range(n):

        entry = 0
        for j in range(n):
            entry += matrix[j][i]

        print(entry, sum(matrix[i]))

