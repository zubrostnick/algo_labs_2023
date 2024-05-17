from math import ceil, log2

class SegmentTree:

    def __init__(self, array):
        m = len(array)
        n = 1 << ceil(log2(m))
        self.items = [0] * n + array + [0] * (n-m)
        print(self.items)
        for i in range(n - 1, 0, -1):
            self.items[i] = self.items[i * 2] + self.items[i * 2 + 1]

        self.size = n

    def sum(self, left, right):
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left % 2 == 1: ## лівий є правим сином
                result += self.items[left]
            if right % 2 == 0: ## правий є ліним сином
                result += self.items[right]
            left = (left + 1) // 2
            right = (right - 1) // 2
        return result
