"""
https://www.eolymp.com/en/submissions/13807813
"""


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        hanging_vertices = 0

        for vertex in range(1, n + 1):
            adjacency_matrix_row = list(map(int, f.readline().split()))
            if sum(adjacency_matrix_row) == 1:
                hanging_vertices += 1

    print(hanging_vertices)
