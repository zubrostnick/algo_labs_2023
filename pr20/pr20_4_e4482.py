"""
https://www.eolymp.com/uk/submissions/13773072
"""


from math import log2, ceil


class DoubleSegmentTree:
    def __init__(self, array):
        m = len(array)
        n = 1 << ceil(log2(m))
        element = array[-1]
        self.items_gcd = [0] * n + array + [element] * (n - m)
        self.items_prod = [1] * n + array + [1] * (n - m)

        for i in range(n - 1, 0, -1):
            self.items_gcd[i] = DoubleSegmentTree.gcd(self.items_gcd[i * 2], self.items_gcd[i * 2 + 1])
            self.items_prod[i] = self.items_prod[i * 2] * self.items_prod[i * 2 + 1]
        self.size = n

    @staticmethod
    def gcd(a, b):
        if a == 0:
            return b
        return DoubleSegmentTree.gcd(b % a, a)

    def execute(self, left, right):
        left += self.size
        right += self.size
        result_gcd = self.items_gcd[left]  # деякий елемент (який не буде впливати на результат)
        result_prod = 1
        if left == right:
            return "draw"

        while left <= right:
            if left % 2 == 1:
                result_gcd = DoubleSegmentTree.gcd(self.items_gcd[left], result_gcd)
                result_prod *= self.items_prod[left]
            if right % 2 == 0:  # якщо правий є лівою дитиною
                result_gcd = DoubleSegmentTree.gcd(self.items_gcd[right], result_gcd)
                result_prod *= self.items_prod[right]
            left = (left + 1) // 2
            right = (right - 1) // 2
        result_lcm = result_prod / result_gcd

        if result_gcd < result_lcm:
            return "wins"
        elif result_gcd == result_lcm:
            return "draw"
        else:
            return "loser"

    def update(self, i, item):
        i += self.size
        self.items_prod[i] = item
        self.items_prod[i] = item
        while i > 1:
            i = i // 2
            self.items_gcd[i] = DoubleSegmentTree.gcd(self.items_gcd[i * 2], self.items_gcd[i * 2 + 1])
            self.items_prod[i] = self.items_prod[i * 2] * self.items_prod[i * 2 + 1]


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        tree = DoubleSegmentTree(arr)
        for _ in range(int(f.readline())):
            command, x, y = f.readline().split()
            x = int(x)
            y = int(y)
            if command == "1":
                print(tree.execute(x - 1, y - 1))
            elif command == "2":
                tree.update(x - 1, y)
