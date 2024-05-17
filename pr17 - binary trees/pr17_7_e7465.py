"""
https://www.eolymp.com/uk/submissions/13663191
"""


class SearchTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        node = self
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = SearchTree(key)
                    break
                else:
                    node = node.left
            elif key >= node.key:
                if node.right is None:
                    node.right = SearchTree(key)
                    break
                else:
                    node = node.right

    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.print()

    def is_equal(self, tree):
        if self.key != tree.key:
            return False

        if self.left is not None and tree.left is not None:
            left_res = self.left.is_equal(tree.left)
        elif self.left is None and tree.left is None:
            left_res = True
        else:
            left_res = False

        if self.right is not None and tree.right is not None:
            right_res = self.right.is_equal(tree.right)
        elif self.right is None and tree.right is None:
            right_res = True
        else:
            right_res = False

        return right_res and left_res


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        keys1 = list(map(int, f.readline().split()))
        m = int(f.readline())
        keys2 = list(map(int, f.readline().split()))

    if n != m:
        print(0)
    else:
        tree1 = SearchTree(keys1[0])
        for i in range(1, n):
            tree1.insert(keys1[i])

        tree2 = SearchTree(keys2[0])
        for i in range(1, m):
            tree2.insert(keys2[i])

        print(int(tree1.is_equal(tree2)))
