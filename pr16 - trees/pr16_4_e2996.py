"""
https://www.eolymp.com/uk/submissions/13602913
"""

from collections import deque


class Tree:

    def __init__(self, key, bribe=None, parent=None):
        self.key = key
        self.bribe = bribe
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

    def add(self, parent_key, key, bribe=0):
        parent = self.bfs(parent_key)  # пошук батьківського
        node = Tree(key, bribe, parent)
        parent.children.append(node)

    def execute(self, curr_bribe=0):
        global answer
        # На основі алгоритму пошуку в глибину
        # print(self.key, curr_bribe, self.bribe)
        curr_bribe += self.bribe

        if not self.children:
            if answer > curr_bribe:
                answer = curr_bribe
                return

        for child in self.children:
            child.execute(curr_bribe)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        tree_data = []
        for i in range(1, n + 1):
            bribe, k, *children = map(int, f.readline().split())
            tree_data.append((i, bribe, children))

    tree = Tree(tree_data[0][0], tree_data[0][1])
    for node_data in tree_data:
        parent_key = node_data[0]
        for child in node_data[2]:
            tree.add(parent_key, child, tree_data[child - 1][1])

    answer = 10 ** 10
    tree.execute()
    print(answer)
