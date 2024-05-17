class Graph:

    def __init__(self, size):
        self.vertices = {
            v: [] for v in range(1, size + 1)
        }

    def add_edge(self, source, destination):
        self.vertices[source].append(destination)


if __name__ == "__main__":
    graph = Graph(3)
    print(graph.vertices)
