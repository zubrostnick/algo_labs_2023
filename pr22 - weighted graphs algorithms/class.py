from collections import deque

"""
"""


# class Graph:
#
#     def __init__(self, matrix):
#         self.matrix = matrix
#         self.n = len(matrix)
#
#     def distance(self, start, finish):
#         queue = deque([start])
#         distances = {start: 0}
#         while queue:
#             i = queue.popleft()
#             if i == finish:
#                 return distances[finish]
#             for j in range(self.n):
#                 if matrix[i][j] == 1 and j not in distances:
#                     queue.append(j)
#                     distances.[j] = distances[i] + 1 # відстань від поточної + 1
#         # Отримуємо словник з найкоротшими відстанями. Дійсно найкоротші, бо алгоритм - пошук завширшки, проходить по
#         # всім сусідам. Тобто значення фіксується на найменшій глибині, а потім навіть не переглядається
#         return 0 # можна стверджувати, що дістатися до врешини не можна, тому повертаємо 0
#
#
#
#
# if __name__ == "__main__":
#     with open("input.txt") as f:
#         n, s, f = map(int, f.readline().split())
#         matrix = []
#         for _ in range(n):
#             matrix.append([int(a) for a in f.readline().split()])
#
#         graph = Graph(matrix)
#         graph.distance(s - 1, f - 1)


from collections import deque

"""
"""


class Graph:

    def __init__(self, size):
        self.vertices = {
            v: set() for v in range(0, size)
        }

    def add_edge(self, u, v):
        self.vertices[u].add(v)
        

    def distance(self, start, finish):
        queue = deque([start])
        distances = {start: 0}
        while queue:
            i = queue.popleft()
            if i == finish:
                return distances[finish]
            for j in range(self.n):
                if matrix[i][j] == 1 and j not in distances:
                    queue.append(j)
                    distances.[j] = distances[i] + 1 # відстань від поточної + 1
        # Отримуємо словник з найкоротшими відстанями. Дійсно найкоротші, бо алгоритм - пошук завширшки, проходить по
        # всім сусідам. Тобто значення фіксується на найменшій глибині, а потім навіть не переглядається
        return 0 # можна стверджувати, що дістатися до врешини не можна, тому повертаємо 0




if __name__ == "__main__":
    with open("input.txt") as f:
        n, s, f = map(int, f.readline().split())
        matrix = []
        for _ in range(n):
            matrix.append([int(a) for a in f.readline().split()])

        graph = Graph(matrix)
        graph.distance(s - 1, f - 1)
