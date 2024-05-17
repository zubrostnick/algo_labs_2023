from collections import deque

"""
https://www.eolymp.com/uk/submissions/13814263
"""

class Solver:

    def bfs(self, a, b):
        self.queue = deque([a])

        self.parent = {a: None}

        while self.queue:
            i = self.queue.popleft()

            if i // 1000 != 9:
                n = (i // 1000 + 1) * 1000 + i % 1000
                if self.bfs_helper(n, i, b):
                    break

            if i % 10 != 1:
                n = i - 1
                if self.bfs_helper(n, i, b):
                    break

            n = i // 10 + (i % 10) * 1000
            if self.bfs_helper(n, i, b):
                break

            n = (i % 1000) * 10 + (i // 1000)
            if self.bfs_helper(n, i, b):
                break


        sequence = []
        while b != a:
            sequence.append(b)
            b = self.parent[b]
        sequence.append(a)

        print(*sequence[::-1], sep='\n')

    def bfs_helper(self, n, i, b):
        if n == b and n not in self.parent:
            self.parent[n] = i
            self.queue.append(n)
            return True

        elif n == b:
            return True

        elif n not in self.parent:
            self.parent[n] = i
            self.queue.append(n)
            return False

        elif n in self.parent:
            return False


if __name__ == "__main__":
    with open("input.txt") as f:
        a = int(f.readline())
        b = int(f.readline())

    s = Solver()
    s.bfs(a, b)

