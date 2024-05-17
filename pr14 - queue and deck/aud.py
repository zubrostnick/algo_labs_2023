# class Deque:
#
#     def __init__(self, maxsize):
#         self._items = [None for _ in range(maxsize)]
#         self._front = 0
#         self._back = 0
#         self._size = 0
#
#     def push(self, item):
#         if self._size > 0:
#             self._back = (self._back + 1) % len(self._items)
#         self._items[self._back] = item
#         self._size += 1
#         #self._items.append(item)
#         return "ok"
#
#     def pop(self):
#         item = self._front # запам'ятовуємо елемент, який хочемо повернути
#         self._items[self._front] = None # None можемо не записувати (- одна операція)
#         if self._size > 1:
#             self._front = (self._front + 1) % len(self._items)
#         self._size -= 1
#         return item
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
        self._back.next = node
        self.size += 1

    def pop(self):
        node = self._front
        self._front = self._front.next
        if self._size == 1:
            self.back = None
        self._size -= 1
        return node.item

    def size(self):
        return self._size

    def clear(self):
        self.__init__()
        return "ok"



        #return self._items.pop(0)