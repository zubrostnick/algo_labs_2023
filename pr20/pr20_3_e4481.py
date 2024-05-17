"""
https://www.eolymp.com/uk/submissions/13772798
"""


from math import log2, ceil


class SegmentTree:

    def __init__(self, array):
        m = len(array)
        n = 1 << ceil(log2(m))
        element = array[-1]
        self.items = [0] * n + array + [element] * (n - m)
        for i in range(n - 1, 0, -1):
            self.items[i] = SegmentTree.gcd(self.items[i * 2], self.items[i * 2 + 1])
        self.size = n

    @staticmethod
    def gcd(a, b):
        if a == 0:
            return b
        return SegmentTree.gcd(b % a, a)

    def execute(self, left, right):
        left += self.size
        right += self.size
        result = self.items[left]  # деякий елемент (який не буде впливати на результат)
        while left <= right:
            if left % 2 == 1:
                result = SegmentTree.gcd(self.items[left], result)
            if right % 2 == 0:
                result = SegmentTree.gcd(self.items[right], result)
            left = (left + 1) // 2
            right = (right - 1) // 2
        return result

    def update(self, i, item):
        i += self.size
        self.items[i] = item
        while i > 1:
            i = i // 2
            self.items[i] = SegmentTree.gcd(self.items[i * 2], self.items[i * 2 + 1])


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        tree = SegmentTree(arr)
        for _ in range(int(f.readline())):
            command, x, y = f.readline().split()
            x = int(x)
            y = int(y)
            if command == "1":
                print(tree.execute(x - 1, y - 1))
            elif command == "2":
                tree.update(x - 1, y)