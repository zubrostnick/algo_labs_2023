class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
        else:
            self._back.next = node
        self._back = node
        self._size += 1

    def pop(self):
        if self._size == 0:
            return "error"
        node = self._front
        self._front = self._front.next
        if self._size == 1:
            self._back = None
        self._size -= 1
        return node.item

    def front(self):
        if self._size == 0:
            return "error"
        return self._front.item

    def size(self):
        return self._size

    def clear(self):
        self.__init__()



if __name__ == "__main__":
    mod = 10**6
    n, a, b, c, xi_next = map(int, input().split())
    q = Queue()
    s = 0
    for i in range(n):
        xi = xi_next
        xi_next = ((a * xi * xi + b * xi + c) // 100) % mod
        if xi_next % 5 < 2:
            if q.size() >= 1:
                s -= q.pop()
        else:
            q.push(xi_next)
            s += xi_next

    print(s)




