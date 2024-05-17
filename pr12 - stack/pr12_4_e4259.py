"""
eolymp.com/uk/submissions/13476872
"""

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):  # додавання елементу в стек
        m = item if not self._items else min(item, self._items[-1][1])
        self._items.append((item, m))

    def pop(self):  # забирає верхівку стека
        # if not self._items[]:
        #     raise Exception("Stack: 'pop' applied to empty container")
        self._items.pop()

    def min(self):
        return self._items[-1][1]


if __name__ == "__main__":
    stack = Stack()
    n = int(input())
    for _ in range(n):
        method, *args = input().split()
        if method == '1':
            stack.push(int(*args))
        elif method == '2':
            stack.pop()
        elif method == '3':
            print(stack.min())
