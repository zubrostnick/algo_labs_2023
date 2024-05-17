"""
https://www.eolymp.com/uk/submissions/13594154
"""


from collections import deque


class Tree:

    def __init__(self, key, colour=None, parent=None):
        self.key = key
        self.colour = colour
        self.children = []
        self.parent = parent

    def bfs(self, key):
        queue = deque()
        queue.append(self)
        while queue:
            node = queue.popleft()  # забираємо зліва, додаємо зправа
            if node.key == key:
                return node
            for child in node.children:
                queue.append(child)

    def add(self, parent_key, colour, key):
        parent = self.bfs(parent_key)  # пошук батьківського
        node = Tree(key, colour, parent)
        parent.children.append(node)

    def get(self, key_1, key_2):
        node = self.bfs(key_1)
        came_from = None
        while node is not None:
            if node.key == key_2:
                return node.key

            for child in node.children:
                if child is not came_from and child.bfs(key_2) is not None:
                    return node.key

            came_from = node
            node = node.parent


def colours(tree, colours_set):
    colours_set.add(tree.colour)

    for child in tree.children:
        colours(child, colours_set)


if __name__ == "__main__":
    with open("input.txt") as f:
        tree_data = []

        n = int(f.readline())
        for i in range(1, n + 1):
            parent, colour = map(int, f.readline().split())
            tree_data.append((parent, colour, i))

    tree = Tree(0)
    added = []
    to_add = deque([0])
    while to_add:
        parent = to_add.popleft()  # забираємо зліва, додаємо зправа
        for node_data in tree_data:
            if node_data[0] == parent:
                tree.add(*node_data)
                to_add.append(node_data[2])

    result = []

    for i in range(1, n + 1):
        c = set()
        colours(tree.bfs(i), c)
        result.append(len(c))

    print(*result)
