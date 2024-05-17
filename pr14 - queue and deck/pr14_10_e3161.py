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

    def empty(self):
        # Якщо код побудовано правильно, достатно одного із
        # self.left is None / self.right is None
        return self.left is None

    def pushfront(self, item):
        new_node = Node(item)
        new_node.next = self.left  # старий елемент стає наступним
        if not self.empty():
            self.left.prev = new_node # новий елемент стає попереднім для старого
        else:
            self.right = new_node

        self.left = new_node
        self._size += 1

    def pushback(self, item):
        new_node = Node(item)
        new_node.prev = self.right  # старий елемент стає попереднім
        if not self.empty():
            self.right.next = new_node  # новий елемент стає попереднім для старого
        else:
            self.left = new_node

        self.right = new_node
        self._size += 1

    def popfront(self):
        if self.empty():
            return "error" # raise Exception('')
        value = self.left.item
        self.left = self.left.next
        if self.left is None: # якщо був 1 елемент (next -> None)
            self.right = None
        else:
            self.left.prev = None
        self._size -= 1
        print(value)

    def popback(self):
        if self.empty():
            return "error"
        value = self.right.item
        self.right = self.right.prev
        if self.right is None:
            self.left = None
        else:
            self.right.next = None
        self._size -= 1
        print(value)

    def size(self):
        return self._size


if __name__ == "__main__":
    queue = Deque()
    multideck = []
    used_numbers = set()

    with open("input.txt") as f:
        n = int(f.readline())
        for line in f:
            method, number, *args = line.split()
            number = int(number) - 1
            if number not in used_numbers:
                used_numbers.add(number)
                multideck.append(Deque())
            getattr(multideck[number], method)(*args)

