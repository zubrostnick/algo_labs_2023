"""
https://www.eolymp.com/uk/submissions/13682439
"""


class Node:
    def __init__(self, id, priority) -> object:
        self.id = id
        self.priority = priority


class Heap:

    def __init__(self):
        self.items = [None]

    def ADD(self, id, priority):
        item = Node(id, int(priority))
        self.items.append(item)
        self.sift_up(len(self.items) - 1)

    def POP(self):
        if len(self.items) == 1:
            return
        self.swap(1, -1)
        item = self.items.pop()
        # print(self.items)
        self.sift_down(1)
        print(item.id, item.priority)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def sift_up(self, curr):
        while curr > 1:
            parent = curr // 2
            if self.items[curr].priority < self.items[parent].priority:
                break
            self.swap(curr, parent)
            curr = parent

    def sift_down(self, curr):
        while curr * 2 < len(self.items):
            left = curr * 2
            right = left + 1
            if right < len(self.items) and self.items[left].priority < self.items[right].priority:
                child = right
            else:
                child = left
            if self.items[child].priority < self.items[curr].priority:
                break
            self.swap(curr, child)
            curr = child

    def find_elem(self, id):
        for i in range(1, len(self.items)):
            if self.items[i].id == id:
                return i

    def CHANGE(self, id, new_priority):
        index = self.find_elem(id)
        self.items[index].priority = int(new_priority)
        # для відновлення структури Купи
        self.sift_up(index)
        self.sift_down(index)

    def execute(self, command):
        method, *args = command.split()
        getattr(self, method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        heap = Heap()
        for line in f:
            heap.execute(line)
