"""
https://www.eolymp.com/uk/submissions/13682245
"""


class Person:
    def __init__(self, t, w) -> object:
        self.w = w
        self.t = t


class Heap:

    def __init__(self):
        self.items = [None]

    def is_empty(self):
        return len(self.items) == 1

    def insert(self, item):  # item - tuple
        item = Person(*item)
        self.items.append(item)
        self.sift_up()

    def extract_max(self):
        if len(self.items) == 1:
            return
        self.swap(1, -1)
        item = self.items.pop()
        # print(self.items)
        self.sift_down()
        return item

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def sift_up(self):
        curr = len(self.items) - 1
        while curr > 1:
            parent = curr // 2
            if self.items[curr].w < self.items[parent].w:
                break
            self.swap(curr, parent)
            curr = parent

    def sift_down(self):
        curr = 1
        while curr * 2 < len(self.items):
            left = curr * 2
            right = left + 1
            if right < len(self.items) and self.items[right].w > self.items[left].w:
                child = right
            else:
                child = left
            if self.items[child].w < self.items[curr].w:
                break
            self.swap(curr, child)
            curr = child


def execute(stack):
    heap = Heap()
    time = stack[-1][0]
    result = 0
    while True:
        if heap.is_empty() and not stack:
            break

        if heap.is_empty():
            time = stack[-1][0]

        if stack:
            while stack and stack[-1][0] <= time:
                heap.insert(stack.pop())

        next = heap.extract_max()
        result += next.w * (time - next.t)
        time += 1
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        for _ in range(n):
            arr = []
            k = int(f.readline())

            for i in range(k):
                arr.append(tuple(map(int, f.readline().split())))

            print(execute(sorted(arr, reverse=True)))
