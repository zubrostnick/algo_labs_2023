"""

"""


class Node:
    """Допоміжний клас 'Вузол' """
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.left = None
        self.right = None
        self._size = 0

    def clear(self):
        self.__init__()
        #return 'ok'

    def empty(self):
        # Якщо код побудовано правильно, достатно одного із
        # self.left is None / self.right is None
        return self.left is None

    def push_front(self, item):
        new_node = Node(item)
        new_node.next = self.left  # старий елемент стає наступним
        if not self.empty():
            self.left.prev = new_node # новий елемент стає попереднім для старого
        else:
            self.right = new_node

        self.left = new_node
        self._size += 1

    def push_back(self, item):
        new_node = Node(item)
        new_node.prev = self.right  # старий елемент стає попереднім
        if not self.empty():
            self.right.next = new_node  # новий елемент стає попереднім для старого
        else:
            self.left = new_node

        self.right = new_node
        self._size += 1

    def pop_front(self):
        if self.empty():
            return "error" # raise Exception('')
        value = self.left.item
        self.left = self.left.next
        if self.left is None: # якщо був 1 елемент (next -> None)
            self.right = None
        else:
            self.left.prev = None
        self._size -= 1
        return value

    def pop_back(self):
        if self.empty():
            return "error"
        value = self.right.item
        self.right = self.right.prev
        if self.right is None:
            self.left = None
        else:
            self.right.next = None
        self._size -= 1
        return value

    def front(self):
        if self.empty():
            return "error"
        return self.left.item

    def back(self):
        if self.empty():
            return "error"
        return self.right.item

    def size(self):
        return self._size


def execute(deque1, deque2, n):
    turn = 0
    while deque1.size() != 0 and deque2.size() != 0:
        turn += 1
        card1 = deque1.pop_back()
        card2 = deque2.pop_back()
        if card1 == 0 and card2 == n-1:
            deque1.push_front(card1)
            deque1.push_front(card2)
        elif (card2 == 0 and card1 == n-1) or card2 > card1:
            deque2.push_front(card1)
            deque2.push_front(card2)
        else:
            deque1.push_front(card1)
            deque1.push_front(card2)

    if deque1.empty():
        return "second", turn
    else:
        return "first", turn


if __name__ == "__main__":
    n = int(input())
    d1 = Deque()
    for i in map(int, input().split()):
        d1.push_back(i)

    d2 = Deque()
    for i in map(int, input().split()):

        d2.push_back(i)

    print(*execute(d1, d2, n))

