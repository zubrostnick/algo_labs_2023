"""
https://www.eolymp.com/uk/submissions/13477123
"""



class Node:
    def __init__(self, value):
        self.next_node = None
        self.value = value



class Stack:
    def __init__(self):
        self.top_node = None
        self.length = 0

    def push(self, item):
        node = Node(item)
        node.next_node = self.top_node
        self.top_node = node
        self.length += 1
        return "ok"

    def pop(self):
        if self.top_node is None:
            return "error"
        node = self.top_node
        self.top_node = self.top_node.next_node
        self.length -= 1
        return node.value

    def back(self):
        if self.top_node is None:
            return "error"
        return self.top_node.value

    def size(self):
        return self.length

    def clear(self):
        self.__init__()
        return "ok"

    @staticmethod
    def exit():
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    stack = Stack()
    with open("input.txt") as f:
        for line in f:
            result = stack.execute(line)
            print(result)
            if result == "bye":
                break