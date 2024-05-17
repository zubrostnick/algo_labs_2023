"""
https://www.eolymp.com/uk/submissions/13538218
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Doubly_linked_list:
    def __init__(self):
        self.front = None
        self.back = None
        self.curr = None

    def empty(self):
        return self.front is None

    def insert_after(self, item):
        new_node = Node(item)
        if self.empty():
            self.front = self.curr = self.back = new_node
            return
        new_node.prev = self.curr
        new_node.next = self.curr.next

        if self.curr is self.back:  # якщо один елемент
            self.back = new_node
        else:
            self.curr.next.prev = new_node

        self.curr.next = new_node
        self.next()

    def next(self):
        if self.empty() or self.curr.next is None:
            raise StopIteration
        self.curr = self.curr.next

    def print(self):
        node = self.front
        while node is not None:
            print(node.item, end=' ')
            node = node.next
        print()

    def print_reverse(self):
        node = self.back
        while node is not None:
            print(node.item, end=' ')
            node = node.prev
        print()


if __name__ == "__main__":
    n = int(input())
    lst = Doubly_linked_list()
    for elem in map(int, input().split()):
        lst.insert_after(elem)

    lst.print()
    lst.print_reverse()
