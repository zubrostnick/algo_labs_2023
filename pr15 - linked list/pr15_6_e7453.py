"""
https://www.eolymp.com/uk/submissions/13538658
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Linked_list:   # використання двозв'язного кільцевого списку
    def __init__(self):
        self.curr = None

    def empty(self):
        return self.curr is None

    def insert_after(self, item):
        new_node = Node(item)
        if self.empty():
            self.curr = new_node
            self.curr.next = self.curr
            self.curr.prev = self.curr
            return

        new_node.prev = self.curr
        new_node.next = self.curr.next

        self.curr.next.prev = new_node
        self.curr.next = new_node


    def next(self):
        if self.empty() or self.curr.next is None:
            raise StopIteration
        self.curr = self.curr.next

    def prev(self):
        if self.empty() or self.curr.prev is None:
            raise StopIteration
        self.curr = self.curr.prev

    def print(self, k, n):
        for _ in range(k % n):
            self.prev()

        first_node = self.curr
        print(first_node.item, end=' ')

        node = self.curr.next
        while node is not first_node:
            print(node.item, end=' ')
            node = node.next

        print()


if __name__ == "__main__":
    if __name__ == "__main__":
        lst = Linked_list()
        with open("input.txt") as f:
            n = int(f.readline())
            for elem in map(int, f.readline().split()):
                lst.insert_after(elem)
                lst.next()
            lst.next()
            for line in f:
                lst.print(int(line.strip()), n)
