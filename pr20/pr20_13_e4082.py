"""https://www.eolymp.com/uk/submissions/13774042"""

from math import log2, ceil


class SegmentTree:

    def __init__(self, array):
        m = len(array)
        n = 1 << ceil(log2(m))
        self.items = [1] * n + array + [1] * (n - m)
        for i in range(n - 1, 0, -1):
            self.items[i] = self.items[i * 2] * self.items[i * 2 + 1]
        self.size = n

    def execute(self, left, right):
        left += self.size
        right += self.size
        result = 1
        while left <= right:
            if left % 2 == 1:  # Лівий є правим сином
                result *= self.items[left]
            if right % 2 == 0:  # Правий є лівим сином
                result *= self.items[right]
            left = (left + 1) // 2
            right = (right - 1) // 2

        if result == 0:
            return "0"
        elif result > 0:
            return "+"
        else:
            return "-"

    def update(self, i, item):
        i += self.size
        self.items[i] = item
        while i > 1:
            i = i // 2
            self.items[i] = self.items[i * 2] * self.items[i * 2 + 1]


if __name__ == "__main__":
    with open("input.txt") as f:
        while True:
            try:
                n, q = map(int, f.readline().split())
                arr = list(map(int, f.readline().split()))
                tree = SegmentTree(arr)
                for _ in range(q):
                    command, x, y = f.readline().split()
                    x = int(x)
                    y = int(y)
                    if command == "P":
                        print(tree.execute(x - 1, y - 1), end="")
                    elif command == "C":
                        tree.update(x - 1, y)
                print()
            except:
                break

